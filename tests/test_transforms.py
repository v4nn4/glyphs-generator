from glyphs_generator import Stroke, Glyph, GlyphGenerator


def test_flip_horizontal(basic_generator: GlyphGenerator) -> None:
    generator = basic_generator
    (th, lv, d1, d2, rv, bh) = [generator.from_stroke(x) for x in generator.parent_strokes]

    for stroke in [th, lv, rv, bh]:
        assert stroke in generator.transform(th)

    for stroke in [d1, d2]:
        assert stroke in generator.transform(d1)

    transformed = generator.transform(lv | bh | d1)
    assert (rv | th | d1) in transformed


def test_equal(advanced_generator: GlyphGenerator) -> None:
    generator = advanced_generator
    g1 = generator.from_glyph(
        Glyph(
            strokes=[
                Stroke(x0=-1, y0=-1, x1=-1, y1=1),
                Stroke(x0=-1, y0=1, x1=1, y1=1),
            ]
        )
    )
    g2 = generator.from_glyph(
        Glyph(
            strokes=[
                Stroke(x0=-1, y0=-1, x1=-1, y1=1),
                Stroke(x0=-1, y0=1, x1=1, y1=1),
            ]
        )
    )
    transformed_g1 = generator.transform(glyph=g1)
    assert any([g == g2 for g in transformed_g1])

    g1 = generator.from_glyph(
        Glyph(
            strokes=[
                Stroke(x0=-1, y0=-1, x1=-1, y1=1),
                Stroke(x0=-1, y0=0, x1=1, y1=0),
                Stroke(x0=-1, y0=1, x1=1, y1=1),
            ]
        )
    )
    g2 = generator.from_glyph(
        Glyph(
            strokes=[
                Stroke(x0=-1, y0=-1, x1=-1, y1=1),
                Stroke(x0=0, y0=1, x1=0, y1=-1),
                Stroke(x0=-1, y0=1, x1=1, y1=1),
            ]
        )
    )
    transformed_g1 = generator.transform(glyph=g1)
    assert any([g == g2 for g in transformed_g1])
