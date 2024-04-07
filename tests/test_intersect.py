from glyphs_generator import do_intersect, GlyphGenerator


def test_intersect():
    assert do_intersect(-1, -1, 1, 1, 1, 1, -1, -1)
    assert do_intersect(-1, -1, -1, 1, -1, 1, 1, 1)
    assert not do_intersect(-1, -1, -1, 1, 1, -1, 1, 1)


def test_intersection(basic_generator: GlyphGenerator):
    generator = basic_generator
    (th, lv, d1, d2, rv, bh) = [generator.from_stroke(x) for x in generator.parent_strokes]
    assert not generator.are_strokes_intersecting(th | bh)
    assert not generator.are_strokes_intersecting(lv | rv)
    assert generator.are_strokes_intersecting(d1 | d2)
    assert generator.are_strokes_intersecting(lv | d1)
    assert generator.are_strokes_intersecting(bh | d2)
    assert generator.are_strokes_intersecting(rv | th)
    assert generator.are_strokes_intersecting(th | lv | d1 | d2 | rv | bh)
