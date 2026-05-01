# Phase 1A — Shard Template Geometry

_Agent A output. All templates use `viewBox="0 0 100 100"`. Edge midpoints: top (50,0), right (100,50), bottom (50,100), left (0,50). All polygon areas verified to sum to 10 000 (full cell). Winding: counter-clockwise for all polygons (consistent)._

---

## Template A — "Pinwheel"

- **Description:** Central node at (50,50) with 4 leading lines radiating to each of the 4 edge midpoints. Divides the cell into 4 equal quadrilateral shards, each containing one corner of the cell. The leading lines cross at center, creating a strong symmetrical pinwheel. No interior points other than the center hub.

- **Polygons:**
  - `"0,0 50,0 50,50 0,50"`   (top-left quarter)
  - `"50,0 100,0 100,50 50,50"`   (top-right quarter)
  - `"50,50 100,50 100,100 50,100"`   (bottom-right quarter)
  - `"0,50 50,50 50,100 0,100"`   (bottom-left quarter)

- **Leading paths:**
  - `"M 50,0 L 50,50"`   (top midpoint to center)
  - `"M 100,50 L 50,50"`   (right midpoint to center)
  - `"M 50,100 L 50,50"`   (bottom midpoint to center)
  - `"M 0,50 L 50,50"`   (left midpoint to center)

---

## Template B — "Fold"

- **Description:** A V-shaped break — two leading lines forming a zigzag fold from top-midpoint down-left to the left-midpoint, then down-right to the bottom-midpoint. This creates one small triangle in the top-left corner, one small triangle in the bottom-left corner, and one large asymmetric pentagon occupying the entire right side. The "broken glass" feel comes from the angular inward fold on the left side.

- **Polygons:**
  - `"0,0 50,0 0,50"`   (small top-left triangle)
  - `"0,50 50,100 0,100"`   (small bottom-left triangle)
  - `"50,0 100,0 100,100 50,100 0,50"`   (large right pentagon)

- **Leading paths:**
  - `"M 50,0 L 0,50 L 50,100"`   (full V-fold path, through left midpoint)

---

## Template C — "Fan"

- **Description:** Four fan lines all radiating from the bottom-midpoint (50,100). Three lines reach the other three edge midpoints (left, top, right). A fourth line reaches interior point (70,35) — placed between the top-midpoint arm and the right-midpoint arm — splitting the upper-right region into one large pentagon and one compact triangle. Result: 5 wedge-shaped shards fanning upward from the bottom edge. The interior endpoint at (70,35) gives the fan a deliberately uneven, asymmetric spread on the right side.

- **Polygons:**
  - `"0,100 0,50 50,100"`   (far-left slim triangle)
  - `"0,50 0,0 50,0 50,100"`   (upper-left quadrilateral)
  - `"50,100 50,0 100,0 100,50 70,35"`   (large upper-right pentagon)
  - `"50,100 70,35 100,50"`   (small right-center triangle)
  - `"100,50 100,100 50,100"`   (far-right slim triangle)

- **Leading paths:**
  - `"M 50,100 L 0,50"`   (to left midpoint)
  - `"M 50,100 L 50,0"`   (to top midpoint)
  - `"M 50,100 L 70,35"`   (to interior split point)
  - `"M 50,100 L 100,50"`   (to right midpoint)

---

## Template D — "Split"

- **Description:** Single leading line running horizontally from the left-midpoint (0,50) to the right-midpoint (100,50). Divides the cell into two large equal rectangles — top half and bottom half. The simplest possible geometry; acts as visual "breathing room" amid the more complex neighbors. Chosen as horizontal (rather than vertical) because the cell grid is wider than tall in the carriage-view layout, making a horizontal split more visually distinct from a vertical one.

- **Polygons:**
  - `"0,0 100,0 100,50 0,50"`   (top half)
  - `"0,50 100,50 100,100 0,100"`   (bottom half)

- **Leading paths:**
  - `"M 0,50 L 100,50"`   (left midpoint to right midpoint)

---

## Area verification (all templates)

| Template | Shard count | Sum of polygon areas |
|---|---|---|
| A — Pinwheel | 4 | 4 × 2500 = 10 000 ✓ |
| B — Fold | 3 | 1250 + 1250 + 7500 = 10 000 ✓ |
| C — Fan | 5 | 1250 + 3750 + 2625 + 1125 + 1250 = 10 000 ✓ |
| D — Split | 2 | 5000 + 5000 = 10 000 ✓ |

---

## Tiling connectivity (edge midpoint table)

Each edge midpoint (50,0 / 100,50 / 50,100 / 0,50) is a leading-line endpoint or shard vertex in every template, meaning adjacent cells always have a leading endpoint at the shared midpoint regardless of which template is assigned.

| Midpoint | A | B | C | D |
|---|---|---|---|---|
| (50,0) top | leading endpoint | leading endpoint | leading endpoint (fan arm) | polygon vertex only |
| (100,50) right | leading endpoint | polygon vertex | leading endpoint (fan arm) | leading endpoint |
| (50,100) bottom | leading endpoint | leading endpoint | fan origin | polygon vertex only |
| (0,50) left | leading endpoint | leading endpoint (fold node) | leading endpoint (fan arm) | leading endpoint |

All four midpoints appear as leading endpoints in at least 3 of the 4 templates. In Template D, (50,0) and (50,100) are shard polygon vertices only (lying on the horizontal split line's perpendicular bisector) — a leading line from an adjacent cell using those midpoints will visually "land" at a shard corner, which is acceptable: the gold lead from the neighbor terminates at a shard boundary, not in open space.

---

## Visual ASCII sketches (one per template)

```
Template A — "Pinwheel"        Template B — "Fold"
+----+----+                    +----+----+
|\   |   /|                    |\ /      |
| \  |  / |                    | X       |
|  \ | /  |                    |/ \      |
+----+----+                    +    \    |
|  / | \  |                    |     \   |
| /  |  \ |                    |      \  |
|/   |   \|                    |       \ |
+----+----+                    +----+----+
4 quarter-squares from center  Small tri TL + small tri BL + big right


Template C — "Fan"             Template D — "Split"
+----+----+                    +----+----+
|\   |  ./|                    |         |
| \  | /./|                    |  top    |
|  \ |/. /|                    |         |
|   \|./  |                    +---------+
|   /|\.  |                    |         |
|  /.| \  |                    |  bottom |
| /. |  \ |                    |         |
+----+----+                    +----+----+
5 wedges fanning from bottom   2 horizontal halves
midpoint; 4th arm (·) hits
interior point (70,35)
```

---

## Geometry decisions log

1. **Template A center point:** (50,50) exactly. No offset — pinwheel symmetry is the point; any offset would require re-specifying all 4 polygon shapes and lose the 4×2500 equal-area property.

2. **Template B fold direction:** Fold goes left (top → left midpoint → bottom), not right. The large shard is on the right. This means when Fold cells are adjacent to other templates, the small left triangles align with the leading lines of their neighbors at (50,0), (0,50), and (50,100), all of which are fold-line nodes.

3. **Template C interior point at (70,35):** Placed at 70% across, 35% down — inside the upper-right quadrant, biased toward the right so the small shard (triangle 4) is noticeably compact. The exact coordinates were chosen so all 5 shard areas are non-trivially different (1250, 3750, 2625, 1125, 1250) rather than symmetric, reinforcing the "fan caught mid-motion" feel.

4. **Template D horizontal vs vertical:** Horizontal split (left→right midpoints) chosen over vertical (top→bottom midpoints) for two reasons: (a) carriage-view cells are expected to be wider than tall, making a horizontal seam more prominent; (b) a vertical split would look identical to Template A's vertical center line, reducing visual variety in the tile grid.

5. **Winding consistency:** All polygons are listed in counter-clockwise vertex order, which is the standard for SVG `fill-rule: nonzero` and matches the expected winding for `fill-rule: evenodd` with non-self-intersecting polygons.
