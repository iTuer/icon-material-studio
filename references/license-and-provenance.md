# License and provenance record

Use this reference when source assets or commercial rights matter. Check the primary source's current license and the exact file's page. If the distribution index and author page disagree, record the conflict and treat commercial clearance as unresolved. A license for the icon's outline may still apply after recolor or image generation based on that outline. A screenshot used as a generation input also needs provenance; style-only use is not a blanket rights guarantee.

For each final asset, record:

| Field | Meaning |
|---|---|
| `file` | Delivered filename or Figma node |
| `subject` | User-facing icon meaning |
| `source_url` | Direct original icon/image URL, or `none: text-only original brief` |
| `creator` | Source author/library, if known |
| `license_url` | Primary license page, or `unknown` |
| `source_role` | Modified shape / style reference / edit target / none |
| `commercial_status` | Cleared with conditions / unclear / noncommercial / purchase or permission required |
| `cost` | Free, paid, generation service cost, or unknown; do not infer a price |
| `attribution` | Required text/link and modification note, or none/unknown |
| `generation` | Tool, material, prompt summary, and parent output if any |
| `verification` | Date checked, file properties, size preview |

Use plain labels in the response: **可免费商用（附条件）**, **需购买或取得授权**, **仅非商用**, **授权未确认**, **AI 生成（非开源素材）**. Do not collapse all “free” items into commercial-safe. If the user asks for commercially usable work, exclude unresolved candidates from the final commercial-ready package and tell them what was excluded.

An attribution text should name the library/creator, link the original and license, and note modifications where required. Include it in a separate `CREDITS.md` or manifest for packaged assets; do not imply attribution on the icon itself is sufficient or always needed.
