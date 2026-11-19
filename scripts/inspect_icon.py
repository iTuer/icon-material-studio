#!/usr/bin/env python3
"""
Read-only icon inspector and light/dark multi-size preview generator.
Does NOT modify or overwrite the input image's alpha channel or pixels.

Usage:
    python3 scripts/inspect_icon.py <path/to/icon.png> [--out-dir <preview_dir>]
"""

import argparse
import base64
import json
import html as html_lib
import os
import struct
import sys
import zlib


def parse_png_rgba(path: str):
    """Parse an 8-bit RGBA PNG using only the Python standard library."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a valid PNG file.")

    pos = 8
    width = height = bit_depth = color_type = interlace = 0
    idat_chunks = bytearray()

    seen_ihdr = seen_iend = False
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValueError("Truncated PNG chunk header")
        length, chunk_type = struct.unpack(">I4s", data[pos : pos + 8])
        chunk_data = data[pos + 8 : pos + 8 + length]
        if length > len(data) - pos - 12:
            raise ValueError("Truncated PNG chunk data")
        stored_crc = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])[0]
        if (zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF) != stored_crc:
            raise ValueError("PNG chunk CRC mismatch")
        if not seen_ihdr and chunk_type != b"IHDR":
            raise ValueError("IHDR must be first")
        if chunk_type == b"IHDR":
            if seen_ihdr or length != 13:
                raise ValueError("Invalid or duplicate IHDR")
            seen_ihdr = True
            width, height, bit_depth, color_type, compression, filtering, interlace = struct.unpack(
                ">IIBBBBB", chunk_data[:13]
            )
            if width == 0 or height == 0 or compression != 0 or filtering != 0 or interlace not in (0, 1):
                raise ValueError("Invalid PNG header")
        elif chunk_type == b"IDAT":
            idat_chunks.extend(chunk_data)
        elif chunk_type == b"IEND":
            if length != 0 or pos + 12 != len(data):
                raise ValueError("Invalid IEND or trailing data")
            seen_iend = True
            break
        pos += 12 + length

    if not seen_ihdr or not seen_iend or not idat_chunks:
        raise ValueError("Missing required PNG chunks")
    info = {
        "file": os.path.basename(path),
        "width": width,
        "height": height,
        "bit_depth": bit_depth,
        "color_type": color_type,
        "has_alpha": color_type in (4, 6),
        "is_rgba_8bit": (bit_depth == 8 and color_type == 6 and interlace == 0),
    }

    if not info["is_rgba_8bit"]:
        info.update(pixel_inspection="unsupported", warnings=["Pixel inspection supports only non-interlaced 8-bit RGBA PNG. No pixel-quality pass is implied."])
        return info

    expected = height * (width * 4 + 1)
    if expected > 256 * 1024 * 1024:
        raise ValueError("Image exceeds inspector memory limit")
    decoder = zlib.decompressobj()
    raw = decoder.decompress(bytes(idat_chunks), expected + 1)
    if len(raw) != expected or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
        raise ValueError("Invalid PNG decompressed length or zlib stream")
    stride = width * 4
    prev_row = bytearray(stride)
    cur_row = bytearray(stride)

    transparent_px = 0
    opaque_px = 0
    near_opaque_px = 0
    semi_px = 0
    bright_fringe_px = 0

    min_x, min_y = width, height
    max_x, max_y = -1, -1

    offset = 0
    for y in range(height):
        filter_type = raw[offset]
        offset += 1
        row_bytes = raw[offset : offset + stride]
        offset += stride

        if filter_type == 0:
            cur_row[:] = row_bytes
        elif filter_type == 1:  # Sub
            for i in range(stride):
                left = cur_row[i - 4] if i >= 4 else 0
                cur_row[i] = (row_bytes[i] + left) & 0xFF
        elif filter_type == 2:  # Up
            for i in range(stride):
                cur_row[i] = (row_bytes[i] + prev_row[i]) & 0xFF
        elif filter_type == 3:  # Average
            for i in range(stride):
                left = cur_row[i - 4] if i >= 4 else 0
                up = prev_row[i]
                cur_row[i] = (row_bytes[i] + ((left + up) >> 1)) & 0xFF
        elif filter_type == 4:  # Paeth
            for i in range(stride):
                a = cur_row[i - 4] if i >= 4 else 0
                b = prev_row[i]
                c = prev_row[i - 4] if i >= 4 else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                cur_row[i] = (row_bytes[i] + pr) & 0xFF

        else:
            raise ValueError(f"Invalid PNG filter type: {filter_type}")

        prev_row[:] = cur_row

        for x in range(width):
            idx = x * 4
            a = cur_row[idx + 3]
            if a == 0:
                transparent_px += 1
            else:
                if a > 12:
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y < min_y:
                        min_y = y
                    if y > max_y:
                        max_y = y
                if a == 255:
                    opaque_px += 1
                else:
                    semi_px += 1
                    if a >= 250:
                        near_opaque_px += 1
                    r, g, b = cur_row[idx], cur_row[idx + 1], cur_row[idx + 2]
                    if 25 <= a <= 200 and r > 225 and g > 225 and b > 225:
                        bright_fringe_px += 1

    total = width * height
    if max_x >= min_x and max_y >= min_y:
        bbox_w = max_x - min_x + 1
        bbox_h = max_y - min_y + 1
        occ_w = round(bbox_w / width * 100, 1)
        occ_h = round(bbox_h / height * 100, 1)
    else:
        occ_w = occ_h = 0.0

    warnings = []
    if transparent_px / total < 0.15:
        warnings.append("Background may not be transparent (<15% zero-alpha pixels).")
    if max(occ_w, occ_h) > 94.0:
        warnings.append(f"Safe-area margin is tight (occupancy {max(occ_w, occ_h)}% > 94%).")
    elif max(occ_w, occ_h) < 55.0:
        warnings.append(f"Subject appears too small on canvas (occupancy {max(occ_w, occ_h)}% < 55%).")
    if bright_fringe_px / total > 0.02:
        warnings.append(
            f"Detected {round(bright_fringe_px / total * 100, 1)}% bright semi-transparent pixels; global count only, not edge-localized; inspect dark preview, no halo diagnosis is implied."
        )

    info.update(
        {
            "transparent_ratio_pct": round(transparent_px / total * 100, 1),
            "fully_opaque_pct": round(opaque_px / total * 100, 2),
            "near_opaque_pct": round(near_opaque_px / total * 100, 2),
            "semi_transparent_pct": round(semi_px / total * 100, 1),
            "global_bright_semi_pct": round(bright_fringe_px / total * 100, 2),
            "bbox_alpha_threshold": 12,
            "pixel_inspection": "completed_not_visual_approval",
            "bbox_occupancy_pct": {"width": occ_w, "height": occ_h},
            "warnings": warnings,
        }
    )
    return info


def write_preview_html(png_path: str, report: dict, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    with open(png_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    data_uri = f"data:image/png;base64,{b64}"
    filename = report["file"]
    html_path = os.path.join(out_dir, f"{os.path.splitext(filename)[0]}-preview.html")
    name = html_lib.escape(filename)

    html = f"""<!doctype html>
<html lang="zh-CN">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Icon Inspection · {name}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; padding: 32px; background: #f5f2ec; font-family: system-ui, -apple-system, sans-serif; color: #2d2934; }}
  h1 {{ font-size: 20px; margin: 0 0 16px; }}
  .row {{ display: flex; gap: 20px; align-items: stretch; flex-wrap: wrap; }}
  .panel {{ border-radius: 20px; padding: 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; }}
  .light {{ background: #ffffff; border: 1px solid #e7e2da; }}
  .dark {{ background: #26222c; color: #ece8f2; }}
  .checker {{
    background-image: linear-gradient(45deg, #e0ddd7 25%, transparent 25%),
                      linear-gradient(-45deg, #e0ddd7 25%, transparent 25%),
                      linear-gradient(45deg, transparent 75%, #e0ddd7 75%),
                      linear-gradient(-45deg, transparent 75%, #e0ddd7 75%);
    background-size: 16px 16px;
    background-position: 0 0, 0 8px, 8px -8px, -8px 0;
    background-color: #f9f8f6;
  }}
  .sizes {{ display: flex; gap: 18px; align-items: flex-end; }}
  .size-box {{ display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 12px;  }}
  img {{ object-fit: contain; display: block; }}
  pre {{ margin-top: 20px; background: #fff; padding: 16px; border-radius: 12px; font-size: 12px; overflow-x: auto; }}
</style>
<h1>Icon Quality Inspection · {name} ({report["width"]}×{report["height"]})</h1>
<div class="row">
  <div class="panel checker">
    <img src="{data_uri}" width="160" height="160" alt="native">
    <span>Alpha Checkerboard (160px)</span>
  </div>
  <div class="panel light">
    <div class="sizes">
      <div class="size-box"><img src="{data_uri}" width="96" height="96"><span>96px</span></div>
      <div class="size-box"><img src="{data_uri}" width="48" height="48"><span>48px</span></div>
      <div class="size-box"><img src="{data_uri}" width="32" height="32"><span>32px</span></div>
    </div>
    <span>Light UI Surface (#FFFFFF)</span>
  </div>
  <div class="panel dark">
    <div class="sizes">
      <div class="size-box"><img src="{data_uri}" width="96" height="96"><span>96px</span></div>
      <div class="size-box"><img src="{data_uri}" width="48" height="48"><span>48px</span></div>
      <div class="size-box"><img src="{data_uri}" width="32" height="32"><span>32px</span></div>
    </div>
    <span>Dark UI Surface (#26222C)</span>
  </div>
</div>
<details><summary>Native 1:1 on light / dark (scroll to inspect)</summary>
<div style="overflow:auto;max-height:70vh;background:#fff"><img src="{data_uri}" style="width:{report['width']}px;height:{report['height']}px;max-width:none"></div>
<div style="overflow:auto;max-height:70vh;background:#26222c"><img src="{data_uri}" style="width:{report['width']}px;height:{report['height']}px;max-width:none"></div>
</details>
<pre>{html_lib.escape(json.dumps(report, ensure_ascii=False, indent=2))}</pre>
</html>"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return html_path


def main():
    parser = argparse.ArgumentParser(description="Read-only icon inspector and preview generator.")
    parser.add_argument("png_path", help="Path to the RGBA PNG file to inspect.")
    parser.add_argument("--out-dir", default=None, help="Directory to write HTML preview card.")
    args = parser.parse_args()

    try:
        report = parse_png_rgba(args.png_path)
    except (ValueError, OSError, struct.error, zlib.error) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    if args.out_dir:
        preview_file = write_preview_html(args.png_path, report, args.out_dir)
        report["preview_html"] = preview_file

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["is_rgba_8bit"] else 3


if __name__ == "__main__":
    sys.exit(main())
