# User interaction flow

Use this when the request is open-ended or the user responds with short steering messages. Keep the conversation visual and decision-sized.

1. **Opening:** Restate the subject and any known constraints in one sentence. If source rights matter, say the shortlist will carry source links and commercial labels. Start searching immediately.
2. **Shortlist:** Show 2–4 meaningfully different silhouettes or visual families, numbered consistently. Include a small preview where tools allow, exact source links, and a compact license tag: free commercial with conditions, paid, noncommercial, or unverified. Do not make the user read a long catalog.
3. **Choice:** Ask only the next unresolved choice. Examples: “选 01/02/03；材质想用软陶还是透明玻璃？” or “交付 PNG 包还是放进你给的 Figma 文件？” If the user already supplied a Figma URL or said “all,” use it. Explain a material constraint only when it affects their decision, such as glass losing contrast at 24px. Do not offer flat or other materials as output variants inside this skill.
4. **Preview:** Generate one representative icon or a compact set, then show it at its intended sizes. Ask for corrections only when user preference is needed; fix obvious quality defects without asking.
5. **Handoff:** State (a) search channels actually used, (b) original-resource URL and license URL or no-source text generation, (c) direct file download or Figma node link, (d) commercial-use status and attribution, and (e) actual editability. Keep optional next steps separate from the completed result.

If the user replies with an item number, map it to the last numbered shortlist. If they change only material (“茄子，玻璃”), keep the chosen subject and output mode. If they say “都试试,” generate only the stated clay/glass variants and label each; avoid turning that into an open-ended search. If they ask for a commercially safe result, do not quietly select an unknown-license candidate, even if visually attractive. If they explicitly request flat/vector output or neither clay nor glass, route to ordinary tools without this skill.
