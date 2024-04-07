import pytest

from glyphs_generator.data import Point, InternalGlyph, Glyph
from glyphs_generator.build import initialize_generator_parameters
from glyphs_generator.generate import GlyphGenerator


@pytest.fixture(scope="module")
def basic_generator():
    anchor_points = [
        Point(-1, -1),
        Point(-1, 1),
        Point(1, -1),
        Point(1, 1),
    ]
    parameters = initialize_generator_parameters(anchor_points)
    return GlyphGenerator(parameters)


@pytest.fixture(scope="module")
def advanced_generator():
    anchor_points = [
        Point(-1, -1),
        Point(-1, 1),
        Point(1, -1),
        Point(1, 1),
        Point(0, 0),
        Point(-1, 0),
        Point(1, 0),
        Point(0, 1),
        Point(0, -1),
    ]
    parameters = initialize_generator_parameters(anchor_points)
    return GlyphGenerator(parameters)


def from_glyph(generator: GlyphGenerator, glyph: Glyph) -> InternalGlyph:
    internal_strokes = [generator.from_stroke(stroke) for stroke in glyph.strokes]
    internal_glyph = InternalGlyph.empty()
    for stroke in internal_strokes:
        internal_glyph = internal_glyph | stroke
    return internal_glyph
