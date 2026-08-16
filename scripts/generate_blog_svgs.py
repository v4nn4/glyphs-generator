"""Generate the blog post figures as vector SVGs.

All three figures share the same per-glyph cell size so glyphs render at an
identical visual size in the blog post, regardless of how many glyphs each
figure contains.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from glyphs_generator.build import initialize_generator_parameters
from glyphs_generator.data import Glyph, Point, Stroke
from glyphs_generator.generate import GlyphGenerator

# Shared geometry: each glyph occupies a CELL x CELL box; the glyph's
# [-1, 1] coordinates map onto a GLYPH-sized square centered in the cell.
CELL = 34
GLYPH = 22
STROKE_WIDTH = 1.4
COLOR = "#171717"


def glyph_lines(glyph: Glyph, ox: float, oy: float) -> list[str]:
    half = GLYPH / 2
    cx, cy = ox + CELL / 2, oy + CELL / 2
    lines = []
    for s in glyph.strokes:
        x0, y0 = cx + s.x0 * half, cy + s.y0 * half
        x1, y1 = cx + s.x1 * half, cy + s.y1 * half
        lines.append(
            f'<line x1="{x0:g}" y1="{y0:g}" x2="{x1:g}" y2="{y1:g}"/>'
        )
    return lines


def render_svg(rows: list[list[Glyph]], path: str) -> None:
    width = CELL * max(len(row) for row in rows)
    height = CELL * len(rows)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">',
        f'<g stroke="{COLOR}" stroke-width="{STROKE_WIDTH}" '
        f'stroke-linecap="round" fill="none">',
    ]
    for i, row in enumerate(rows):
        for j, glyph in enumerate(row):
            parts.extend(glyph_lines(glyph, j * CELL, i * CELL))
    parts.append("</g></svg>")
    with open(path, "w") as f:
        f.write("\n".join(parts))
    print(f"wrote {path} ({width}x{height})")


def sorted_rows(glyphs: list[Glyph]) -> list[list[Glyph]]:
    by_order: dict[int, list[Glyph]] = {}
    for glyph in glyphs:
        by_order.setdefault(len(glyph.strokes), []).append(glyph)
    return [by_order[k] for k in sorted(by_order)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("outdir")
    args = parser.parse_args()

    anchor_points = [
        Point(-1, -1), Point(-1, 1), Point(1, -1), Point(1, 1), Point(0, 0),
        Point(-1, 0), Point(1, 0), Point(0, 1), Point(0, -1),
    ]
    generator = GlyphGenerator(initialize_generator_parameters(anchor_points))

    # Figure 1: one equivalence class (4 glyphs in a row)
    a = Stroke(-1, -1, -1, 1)
    b = Stroke(-1, -1, 1, -1)
    e = Stroke(-1, 1, 1, 1)
    h = Stroke(1, -1, 1, 1)
    equivalence_class = [
        Glyph(strokes=[a, b]),
        Glyph(strokes=[a, e]),
        Glyph(strokes=[b, h]),
        Glyph(strokes=[e, h]),
    ]
    render_svg([equivalence_class], os.path.join(args.outdir, "glyph-equivalence-class.svg"))

    # Figure 2: all equivalence classes from a 6-stroke set
    strokes6 = [
        Stroke(-1, -1, -1, 1),
        Stroke(1, -1, 1, 1),
        Stroke(-1, 1, 1, 1),
        Stroke(-1, 0, 1, 0),
        Stroke(0, 1, 0, -1),
        Stroke(1, -1, -1, -1),
    ]
    glyphs6 = generator.generate(strokes6, strokes6[0])
    render_svg(sorted_rows(glyphs6), os.path.join(args.outdir, "6-glyph.svg"))

    # Figure 3: all equivalence classes from a larger stroke set
    strokes10 = [
        Stroke(-1, -1, -1, 1),
        Stroke(-1, -1, 1, -1),
        Stroke(-1, 0, 1, 0),
        Stroke(-1, -1, 1, 1),
        Stroke(-1, 1, 1, 1),
        Stroke(0, -1, 0, 1),
        Stroke(1, -1, -1, 1),
        Stroke(1, -1, 1, 1),
    ]
    glyphs10 = generator.generate(strokes10, strokes10[0])
    render_svg(sorted_rows(glyphs10), os.path.join(args.outdir, "10-glyph.svg"))


if __name__ == "__main__":
    main()
