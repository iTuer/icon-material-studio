---
name: icon-material-studio
description: Create consistent 3D-looking soft-clay icons from object names or reference images, with transparent PNG delivery and source/commercial-use records. Use for soft-clay icons or 3D icons with material unspecified; route explicit non-clay or vector requests to ordinary tools.
---

# Icon Material Studio

A subject name or a reference image is sufficient. Produce a rounded soft-clay icon, not a flat or alternative-material variant. Default to natural subject colors and transparent PNG; expand the generation prompt internally. Do not ask for lighting or camera settings.

## 1. Choose by intent, not input format

- **Direct generation (default):** For a simple object name, or a photo used only to identify a generic object, generate from a subject description without mandatory external searches or candidate selection. Record search channels as `none: direct generation` when none were used.
- **Source search:** When the user asks to find assets, compare silhouettes, or replace an unsuitable reference, read [search channels](references/search-channels.md). Prefer verified free commercially usable resources, then clearly labeled paid options. Return candidates when the user asks only for research. If no candidate meets the brief, report the result and offer independent generation as an option. Obtain authorization before purchasing.
- **Uploaded images:** Distinguish subject identification from actual shape/style image input. Record the rights evidence provided; unknown rights mean `授权未确认`, not `仅非商用`. Use `仅非商用` only when the source explicitly has that restriction. Do not assume a matching icon proves all image layers are covered by its license. Follow [provenance](references/license-and-provenance.md).
- **Specified transformation:** When the user gives a source and wants its exact shape retained, assess that source directly. If commercial use is required and the rights for the planned input/edit are unconfirmed or inadequate, keep the transformation pending until permission is verified. Offer a licensed substitute or an independent design as optional alternatives. Use a substitute only if the user chooses it or has already authorized that fallback.

Short replies such as “02”, “purple”, or “try all” steer the current choices. See [interaction](references/user-interaction.md).

## 2. Generate consistent soft clay

Read [soft-clay specification](references/soft-clay-spec.md) and reuse its material and lighting description. Rounded volume, matte-to-satin diffuse response and clear silhouette are the shared visual goals. Numeric parameters are defaults, not exact model controls or acceptance thresholds; adapt for subject geometry and user colors.

Use the host's available image generation tool; in Codex, follow the available `imagegen` skill and built-in image tool. If unavailable, explain the missing capability instead of substituting a flat icon or silently using a paid API.

The optional [calibration image](resources/clay-calibration-sheet.png) may help reduce style variation. It is not a guarantee of cross-model or cross-session consistency. Describe every input's role: calibration for material/light, subject reference for shape. These are natural-language instructions, not independent guaranteed control channels. Check for transferred purple/yellow colors or eggplant/croissant geometry and revise only if observed. Record calibration use separately as used or skipped. Describe generation as text-only only when it received no image inputs.

Historical images in `assets/` are documentation only; never use them as default generation inputs. Unresolved source/reference chains must not enter a commercial-ready asset package. Do not claim zero risk, exclusivity or automatic copyright protection from text-only origin. See [calibration provenance](resources/PROVENANCE.md).

## 3. Inspect first

Run `python3 /path/to/icon-material-studio/scripts/inspect_icon.py <output.png> --out-dir <preview_dir>` using the installed skill directory. It supports non-interlaced 8-bit RGBA PNG pixel inspection and explicitly reports unsupported encodings. Check actual alpha, dimensions, native 1:1 and 32px/48px light/dark previews. The script generates previews; an agent must render and inspect them before claiming visual checks passed.

Fully opaque, near-opaque and other semi-transparent pixels are separate statistics, not automatic quality verdicts. Bright semi-transparent pixel counts are global hints, not detected edge halos. Occupancy uses a documented alpha threshold and can include shadows. Inspect actual body bleed-through, visible dark-background halos, clipping and small-size recognition. Fix or regenerate only confirmed defects; never batch-force alpha or resample merely because the master size is unusual. Preserve original pixels unless a specific edit is requested/needed, and export requested sizes separately.

## 4. Deliver

Save selected PNGs to the requested location or project workspace; provide direct download links and ZIP for sets. Include a compact provenance record: channels actually used (or none), original source and license links (or no source asset), every image input/role including calibration, and source rights separately from AI output terms. Keep the user-facing summary short; detailed records can go in `CREDITS.md`.

“Text + built-in AI material image” is not text-only generation. A photo inspected solely to identify a generic object should be recorded separately from image inputs. Source restrictions/unknowns and generation service terms must be disclosed without promising commercial clearance. Exclude unresolved/noncommercial assets from commercial-ready packages. State the result is a transparent PNG with 3D appearance, not a 3D model. Follow the project's own Git rules for project changes.
