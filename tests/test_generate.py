from glyphs_generator import GlyphGenerator


def test_generate(basic_generator: GlyphGenerator) -> None:
    generator = basic_generator
    (th, lv, d1, d2, rv, bh) = [generator.from_stroke(x) for x in generator.parent_strokes]
    seed = generator.parent_strokes[0]
    glyphs = generator.generate(generator.parent_strokes, seed)

    # order 1
    assert generator.to_glyph(th) in glyphs

    # order 2
    assert generator.to_glyph(th | lv) in glyphs
    assert generator.to_glyph(th | d1) in glyphs

    # order 3
    assert generator.to_glyph(th | lv | d1) in glyphs
    assert generator.to_glyph(th | lv | d2) in glyphs
    assert generator.to_glyph(th | lv | rv) in glyphs
    assert generator.to_glyph(th | d1 | d2) in glyphs
    assert generator.to_glyph(th | d1 | bh) in glyphs

    # order 6
    assert generator.to_glyph(th | lv | d1 | d2 | rv | bh) in glyphs
