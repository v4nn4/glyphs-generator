from functools import reduce
from typing import Dict, List

from .data import Glyph, InternalGlyph, InternalStroke, Stroke


class GlyphGenerator:
    def __init__(
        self,
        parent_strokes: List[Stroke],
        intersection_matrix: List[List[int]],
        transformation_matrix: List[List[int]],
    ):
        self.parent_strokes = parent_strokes
        self.intersection_matrix = intersection_matrix
        self.transformation_table = transformation_matrix
        self.nb_transformations = len(transformation_matrix[0])

    def add(self, glyph1: InternalGlyph, glyph2: InternalGlyph) -> InternalGlyph:
        return InternalGlyph(
            strokes=list(set(glyph1.strokes + glyph2.strokes)),
            identifier=glyph1.identifier | glyph2.identifier,
        )

    def are_strokes_intersecting(self, glyph: InternalGlyph) -> bool:
        indices = [stroke.index for stroke in glyph.strokes]
        for i in indices:
            intersection_found = False
            for j in indices:
                if i != j and self.intersection_matrix[i][j] == 1:
                    intersection_found = True
            if not intersection_found:
                return False
        return True

    def transform(self, glyph: InternalGlyph) -> List[InternalGlyph]:
        result = [InternalGlyph(strokes=[], identifier=0) for _ in range(self.nb_transformations)]
        for i in range(self.nb_transformations):
            for stroke in glyph.strokes:
                stroke_index = self.transformation_table[stroke.index][i]
                result[i].strokes.append(InternalStroke(index=stroke_index))
                result[i].identifier |= 2**stroke_index
        return result

    def to_glyph(self, glyph: InternalGlyph) -> Glyph:
        return Glyph(strokes=[self.parent_strokes[s.index] for s in glyph.strokes])

    def from_glyph(self, glyph: Glyph) -> InternalGlyph:
        strokes = [self.from_stroke(stroke).strokes[0] for stroke in glyph.strokes]
        identifier = 0
        for stroke in strokes:
            identifier |= 2**stroke.index
        return InternalGlyph(strokes, identifier)

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
        glyphs: Dict[int, List[InternalGlyph]] = {i: [] for i in range(n)}
        glyphs[0].append(seed_internal)
        for i, last_glyphs in glyphs.items():
            if i == n - 1:
                break
            for glyph in last_glyphs:
                for stroke in strokes_internal:
                    next_glyph = self.add(glyph, stroke)
                    if self.are_strokes_intersecting(next_glyph):
                        transformed_glyphs = self.transform(next_glyph)
                        if next_glyph not in last_glyphs and all([g not in glyphs[i + 1] for g in transformed_glyphs]):
                            glyphs[i + 1].append(next_glyph)
        return list(map(lambda x: self.to_glyph(x), reduce(lambda x, y: x + y, glyphs.values())))
