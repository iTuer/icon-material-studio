# Soft-clay style defaults

Use shared material/light wording across a set. These are visual starting points; model prompts do not enforce physical parameters or exact pixel ranges.

| Feature | Default | Adaptation |
|---|---|---|
| Material | Matte-to-satin polymer clay, broad diffuse highlights, rounded thick edges | Avoid wet plastic glare, metallic reflection and flat paper appearance |
| Camera | Near-front, slight top tilt around 10–15 degrees | Adapt to recognizable subject geometry; keep a set consistent |
| Shape | A few simple rounded main masses | Do not force every subject into 2–4 parts or remove required semantic details |
| Color | Gently softened natural colors | User palette and object identity take precedence; cream, gray, white and dark colors are allowed; no universal HSB clamp |
| Light | Broad upper-left soft light with subtle ambient fill | No exact measurable highlight-area guarantee; avoid sharp glints |
| Shadow | Minimal local contact shading | Check dark surfaces; do not require a floor or wide baked drop shadow |
| Composition | Centered transparent canvas, about 75–82% longest-dimension occupancy | Adjust for tall/wide subjects and actual visual balance; occupancy is advisory |

## Optional material image

`../resources/clay-calibration-sheet.png` combines previously generated eggplant and croissant examples. It can help guide material, but has not been validated as preventing color/shape transfer or eliminating cross-model drift. Use only when helpful and supported. Explain its role separately from a subject image. Inspect outputs for purple/yellow tint and unwanted fruit/pastry geometry. Do not load historical documentation assets as generation inputs. See `../resources/PROVENANCE.md`.

## Reusable prompt

```text
One standalone 3D-look soft-clay UI icon of [SUBJECT AND KEY PARTS].
Palette: [USER COLORS OR NATURAL SUBJECT COLORS].
Material: rounded thick volumes, smooth matte-to-satin polymer clay, broad soft diffuse highlights, clean part separation; avoid hard shiny plastic and metallic glare.
Composition: near-front with gentle top tilt, centered with generous transparent padding, readable at 32px and 48px. Soft upper-left area lighting, subtle local contact shading, no broad white-matte shadow.
Real transparent background. No unrequested words, faces, outlines, watermark or extra objects.
[IF MATERIAL IMAGE USED: use it for surface and lighting only, not its subject shapes or colors.]
[IF SUBJECT IMAGE USED: describe exactly which silhouette/parts to preserve.]
```

中文可沿用同一结构：主体与关键部件 → 用户配色或自然本色 → 圆润厚实的哑光至半哑光软陶 → 正视轻微俯角与左上柔光 → 安全留白与透明背景 → 分别注明每张输入图片的用途。数值是默认指导，按主体与用户要求调整。
