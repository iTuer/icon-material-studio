# Figma handoff

Read when the output destination is Figma. Use the current Figma connector and its `figma:figma-use` skill; do not hard-code an API that may differ across environments.

1. Identify the file and page from the user's link or active context. Inspect existing pages, components, naming, color variables, and relevant frames before writing.
2. Decide whether the icon is native vector/shape or an imported transparent bitmap. A materialized PNG remains a bitmap layer in Figma. Prefer importing the verified clay/glass render. Native construction is allowed only if the result visibly passes the same clay/glass material checks; simple flat gradients are insufficient. Provide a downloadable image alongside the Figma link.
3. Add a clearly named frame or component per icon with enough safe-area. Keep source/provenance in the handoff manifest or node naming/description where supported. Do not upload a copyrighted source preview as if it were user-owned output.
4. Check icon appearance at its intended UI size and at 1×, including contrast and crop. Return actual node IDs/links and confirm the content is visible in the Figma file.
5. If the user needs both Figma and downloadable assets, export or provide both; mark them as distinct deliverables and check that the versions match.

If the Figma connector cannot import or place the chosen asset in the current session, deliver files with exact steps and state that Figma placement is pending. Never claim a Figma edit from a local file alone.
