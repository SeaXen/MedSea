# Cross-link: `[[../00_Index/Medicine MOC]]`, `[[../00_Index/Davidson Chapter Roadmap]]`

## 1. Purpose
Cross-linking the Cardiology MOC with the **Medicine MOC** and **Davidson Chapter Roadmap** creates a navigable knowledge graph that supports both system-based and chapter-based learning.

## 2. Link Structure
- **Cardiology MOC** lives at `/mnt/tb/Medicine/Cardiology/Cardiology MOC.md`
- **Medicine MOC** at `/mnt/tb/Medicine/00_Index/Medicine MOC.md`
- **Davidson Chapter Roadmap** at `/mnt/tb/Medicine/00_Index/Davidson Chapter Roadmap.md`

## 3. Linking Syntax
### Wikilink (Obsidian)
```markdown
[[../00_Index/Medicine MOC]]
[[../00_Index/Davidson Chapter Roadmap]]
[[../00_Index/Medicine MOC#Cardiology]]
```

### Standard Markdown
```markdown
[Medicine MOC](../00_Index/Medicine%20MOC.md)
[Davidson Chapter Roadmap](../00_Index/Davidson%20Chapter%20Roadmap.md)
```

## 4. Cross-Link Placement
Place cross-links in these locations:
- **Top of Cardiology MOC** (navigation breadcrumb)
- **Top of each section** (e.g., "See: Medicine MOC § Chest Pain")
- **Bottom of each disease file** (related topics)
- **Topic-by-topic** (e.g., pericarditis → Medicine MOC § Pericardial disease)

## 5. Davidson Chapter 16 Mapping
Davidson 24th Ed Chapter 16 = "Cardiac Emergencies"
- Maps to `/16_Cardiac_Emergencies/` folder
- Each Davidson subheading = one MOC topic
- Cross-link each cardiology file to its Davidson subheading

### Example File Cross-links
```markdown
## Related Davidson Content
- [[../00_Index/Davidson Chapter Roadmap#Chapter 16 - Cardiac Emergencies]]
- [[../00_Index/Medicine MOC#Cardiology]]

## See Also
- [[STEMI management]]
- [[Cardiogenic shock]]
- [[Aortic dissection]]
```

## 6. Bidirectional Links
Ensure links work **both ways**:
- Cardiology MOC → Medicine MOC (cardiology section)
- Medicine MOC → Cardiology MOC (specialty section)
- Disease files → both MOCs

## 7. Tag System
Use tags to enable filtering:
- `#cardiology`
- `#cardiac-emergency`
- `#high-yield`
- `#viva`
- `#davidson-chapter-16`
- `#FCPS` / `#MRCP`

> **Pearls**
> - **Wikilinks** make the knowledge graph navigable in Obsidian
> - **Cross-linking** = better recall, supports differential diagnosis
> - **Davidson** for textbook order; **Medicine MOC** for system-based
> - **Tag system** enables quick filtering by topic type
> - Update links whenever new files added
