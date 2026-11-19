# Revision verification — 2026-11-19

- 8 automated tests passed: five PNG row filter variants, exact/near alpha classes, CRC error, invalid filter, truncated chunks, decompressed length mismatch, unsupported encoding and escaped native preview.
- Source bytes are checked unchanged by fixture tests. Existing documentation/calibration PNGs are copied without pixel changes.
- Existing eggplant PNG inspection completed; exact opaque and near-opaque values are now separate.
- HTML preview no longer applies container opacity to images; expandable 1:1 light/dark views added.
- Inspector support: non-interlaced 8-bit RGBA only. Other encodings are explicit unsupported results, CLI exit 3; malformed supported images exit 2. Warnings are review hints, not visual approval.
- Direct generation / source search intent routes reviewed. No mandatory external lookup or backup-link quota for generic objects.
- Calibration image is optional and disclosed as an actual image input. No cross-model style-consistency guarantee; no new cross-model generation experiment was run.
- Historical gallery and croissant case retained as documentation; unresolved reference chains remain disclosed, not commercial-ready assets.
