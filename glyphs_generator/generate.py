from functools import reduce
from typing import Dict, List

from .data import Glyph, InternalGlyph, InternalStroke, Stroke, GeneratorParameters
from .intersect import are_strokes_linked


class GlyphGenerator:
    def __init__(self, parameters: GeneratorParameters):
        self.parent_strokes = parameters.parent_strokes
        self.intersection_matrix = parameters.intersection_matrix
        self.transformation_table = parameters.transformation_matrix
        self.nb_transformations = len(parameters.transformation_matrix[0])

    def are_strokes_intersecting(self, glyph: InternalGlyph) -> bool:
        indices = [stroke.index for stroke in glyph.strokes]
        return are_strokes_linked(indices, self.intersection_matrix)

    def transform(self, glyph: InternalGlyph) -> List[InternalGlyph]:
        result = [InternalGlyph.empty() for _ in range(self.nb_transformations)]
        for i in range(self.nb_transformations):
            for stroke in glyph.strokes:
                stroke_index = self.transformation_table[stroke.index][i]
                glyph_ = InternalGlyph.from_stroke(InternalStroke(index=stroke_index))
                result[i] = result[i] | glyph_
        return result

    def to_glyph(self, glyph: InternalGlyph) -> Glyph:
        return Glyph(strokes=[self.parent_strokes[s.index] for s in glyph.strokes])

    def from_stroke(self, stroke: Stroke) -> InternalGlyph:
        for i, stroke_ in enumerate(self.parent_strokes):
            if (
                stroke_.x0 == stroke.x0
                and stroke_.x1 == stroke.x1
                and stroke_.y0 == stroke.y0
                and stroke_.y1 == stroke.y1
            ) or (
                stroke_.x0 == stroke.x1
                and stroke_.x1 == stroke.x0
                and stroke_.y0 == stroke.y1
                and stroke_.y1 == stroke.y0
            ):
                return InternalGlyph(strokes=[InternalStroke(index=i)], identifier=2**i)
        raise Exception(f"Could not find stroke {stroke} in parent strokes")

    def generate(self, strokes: List[Stroke], seed: Stroke) -> List[Glyph]:
        n = len(strokes)
        seed_internal = self.from_stroke(seed)
        strokes_internal = [self.from_stroke(stroke) for stroke in strokes]
        glyphs: Dict[int, List[InternalGlyph]] = {i + 1: [] for i in range(n)}
        glyphs[1].append(seed_internal)
        for i, last_glyphs in glyphs.items():
            if i == n:
                break
            for glyph in last_glyphs:
                for stroke in strokes_internal:
                    next_glyph = glyph | stroke
                    if (
                        len(next_glyph.strokes) == i + 1
                        and next_glyph not in glyphs[i + 1]
                        and self.are_strokes_intersecting(next_glyph)
                    ):
                        transformed_glyphs = self.transform(next_glyph)
                        if all([g not in glyphs[i + 1] for g in transformed_glyphs]):
                            glyphs[i + 1].append(next_glyph)
        return list(map(lambda x: self.to_glyph(x), reduce(lambda x, y: x + y, glyphs.values())))
