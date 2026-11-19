# Revision verification — 2026-11-19

- 8 automated tests passed: five PNG row filter variants, exact/near alpha classes, CRC error, invalid filter, truncated chunks, decompressed length mismatch, unsupported encoding and escaped native preview.
- Source bytes are checked unchanged by fixture tests. Existing documentation/calibration PNGs are copied without pixel changes.
- Existing eggplant PNG inspection completed; exact opaque and near-opaque values are now separate.
- HTML preview no longer applies container opacity to images; expandable 1:1 light/dark views added.
- Inspector support: non-interlaced 8-bit RGBA only. Other encodings are explicit unsupported results, CLI exit 3; malformed supported images exit 2. Warnings are review hints, not visual approval.
- Direct generation / source search intent routes reviewed. No mandatory external lookup or backup-link quota for generic objects.
- Calibration image is optional and disclosed as an actual image input. No cross-model style-consistency guarantee; no new cross-model generation experiment was run.
- Historical gallery and croissant case retained as documentation; unresolved reference chains remain disclosed, not commercial-ready assets.

## Follow-up acceptance checks

These scenarios were exercised in the current Codex session against the revised instructions. Automatic selection and discovery after a fresh install remain to be verified in a new session.

| Request | Observed result |
|---|---|
| Make a croissant icon | Used built-in image generation with text only. The first PNG showed a faint haze on charcoal despite the inspector returning no warnings. A second generation explicitly removed the outside glow. It produced a 1254 × 1254 RGBA PNG with a clear silhouette at 32px and 48px on light and dark backgrounds. The acceptance image is local. |
| Find commercially usable book shapes | Checked the maintainers' sources. Returned two candidates with exact license links, [Lucide Book Open](https://github.com/lucide-icons/lucide/blob/main/icons/book-open.svg) under its [ISC terms](https://github.com/lucide-icons/lucide/blob/main/LICENSE), and [Tabler Notebook](https://github.com/tabler/tabler-icons/blob/main/icons/outline/notebook.svg) under its [MIT terms](https://github.com/tabler/tabler-icons/blob/main/LICENSE). This search-only request ended with a shortlist. |
| Preserve the exact shape of an image with unconfirmed rights for commercial use | Walked through the decision using the archived croissant photo, whose reuse rights are recorded as unconfirmed. The requested transformation remains pending rights verification. A licensed substitute or an independently designed icon can be offered for the user to choose. No image was sent to the generator for this scenario. |

The calibration image was skipped in the direct generation check. The two generations exercised visual review and targeted retry under one model. Cross-session selection and calibration comparisons remain untested.
