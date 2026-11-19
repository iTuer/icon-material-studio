# Search Channels & Commercial Reference Checks (Text Path)

Read only for source-search or reference-transformation tasks. Simple generic requests use direct generation without required external search. Prefer free commercially usable sources; offer paid alternatives if needed, with actual source/license links. Purchase only with authorization.

## 1. Priority Search Channels

| Priority | Channel | Best For | Verification Rule |
|---|---|---|---|
| 1 | **Installed icon skills & local packages** (e.g., Naive Icons, Lucide, Solar, Tabler) | Fast semantic match and clean UI silhouettes | Verify the package's bundled license AND the upstream artwork license |
| 2 | **User's project repository / design system** | Product silhouette consistency | Confirm whether existing project icons are first-party or imported third-party assets |
| 3 | **Official creator sites & GitHub repositories** | Authoritative SVG/PNG source and explicit license files | Record exact file URL + `LICENSE` URL; check whether artwork/images have separate terms from code |
| 4 | **Icon aggregators** (e.g., Iconify) | Broad keyword/synonym discovery across families | Use for discovery only; trace back to the original icon set and verify its license terms |
| 5 | **Open catalogs** (e.g., OpenMoji, Wikimedia Commons) | Concrete objects, food, nature, everyday items | Inspect the specific file's license, attribution requirements, and trademark restrictions |
| 6 | **Paid commercial marketplaces** (e.g., Noun Project, Flaticon, UI8, Envato) | Specialized subjects when free commercial options fail | Label as **需购买或取得授权** with price/subscription terms and links; never purchase without user approval |

## 2. Search Strategy

1. Query using bilingual semantic terms (Chinese + English) and simple shape descriptors (`filled`, `rounded`, `duotone`, `bold`).
2. Filter by commercial usability upfront:
   - Exclude `"free for personal use only"`, unverified reposts, or conflicting license claims from commercial candidates.
   - Distinguish `"free download"`, `"open source"`, `"free commercial use with attribution"`, and `"public domain (CC0)"`.
3. Stop when the request has enough suitable choices; do not require backup links for a direct-generation request.
4. If no suitable external icon passes commercial checks, report the search channels checked and proceed with an independent text-only generation under the locked soft-clay specification, explicitly noting `source_url: none (independent text generation after search)`.
