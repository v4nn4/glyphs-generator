from glyphs_generator import GlyphGenerator
from .conftest import from_glyph


def test_internal_single_stroke(basic_generator: GlyphGenerator) -> None:
    generator = basic_generator
    for stroke in generator.parent_strokes:
        glyph = generator.to_glyph(generator.from_stroke(stroke))
        stroke_ = glyph.strokes[0]
        assert stroke == stroke_
        glyph_ = generator.to_glyph(from_glyph(generator, glyph))
        assert glyph == glyph_


def test_internal_double_stroke(basic_generator: GlyphGenerator) -> None:
    generator = basic_generator
    for s1 in generator.parent_strokes:
        g1 = generator.from_stroke(s1)
        for s2 in generator.parent_strokes:
            g2 = generator.from_stroke(s2)
            g = g1 | g2
            glyph = generator.to_glyph(g)
            if g1 == g2:
                assert g == g1
            else:
                assert len(g.strokes) == 2
            glyph_ = generator.to_glyph(from_glyph(generator, glyph))
            assert glyph == glyph_

            assert g1 | g2 == g2 | g1
            assert g1 | g2 in [g2 | g1]


def test_internal_triple_stroke(basic_generator: GlyphGenerator) -> None:
    generator = basic_generator
    for s1 in generator.parent_strokes:
        g1 = generator.from_stroke(s1)
        for s2 in generator.parent_strokes:
            g2 = generator.from_stroke(s2)
            for s3 in generator.parent_strokes:
                g3 = generator.from_stroke(s3)
                g = g1 | g2 | g3
                glyph = generator.to_glyph(g)
                glyph_ = generator.to_glyph(from_glyph(generator, glyph))
                assert glyph == glyph_

                assert g1 | g2 | g3 == g2 | g1 | g3 == g1 | g3 | g2 == g2 | g3 | g1 == g3 | g1 | g2 == g3 | g2 | g1
