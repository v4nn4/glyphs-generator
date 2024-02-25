from functools import reduce
from typing import List

import numpy as np

from .glyph import Stroke, Glyph, Alphabet


class GlyphGenerator:
    @staticmethod
    def _are_equivalent(glyph_1: Glyph, glyph_2: Glyph) -> bool:
        glyph_1_rot90 = glyph_1.rot90()
        glyph_1_rot180 = glyph_1_rot90.rot90()
        glyph_1_rot270 = glyph_1_rot180.rot90()
        return (
            glyph_1 == glyph_2
            or glyph_1_rot90 == glyph_2
            or glyph_1_rot180 == glyph_2
            or glyph_1_rot270 == glyph_2
            or glyph_1.flip_left() == glyph_2
            or glyph_1_rot90.flip_left() == glyph_2
            or glyph_1_rot180.flip_left() == glyph_2
            or glyph_1_rot270.flip_left() == glyph_2
            or glyph_1.flip_up() == glyph_2
            or glyph_1_rot90.flip_up() == glyph_2
            or glyph_1_rot180.flip_up() == glyph_2
            or glyph_1_rot270.flip_up() == glyph_2
        )

    def generate(self, strokes: List[Stroke]) -> Alphabet:
        alphabet = {k: [] for k in np.arange(0, len(strokes))}
        alphabet[0].append(Glyph(strokes=[strokes[0]]))
        observed = []
        for order, glyphs in alphabet.items():
            if order == len(strokes) - 1:
                continue
            for glyph in glyphs:
                filtered_strokes = [s for s in strokes if s not in glyph]
                for stroke in filtered_strokes:
                    # Check that stroke intersect with glyph
                    if not glyph.intersect(stroke):
                        continue

                    # Create n-th glypj by adding stroke to n-1-th glyph
                    next_glyph = Glyph(strokes=[stroke] + glyph.strokes)

                    if next_glyph in observed:
                        continue
                    else:
                        observed.append(next_glyph)

                    # Check that glyph is not a previous stored glyph
                    all_glyphs = reduce(list.__add__, alphabet.values())
                    if all(
                        [not self._are_equivalent(next_glyph, g) for g in all_glyphs]
                    ):
                        alphabet[order + 1].append(next_glyph)
        return Alphabet(glyphs=alphabet)
