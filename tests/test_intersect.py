from glyphs_generator import do_intersect, GlyphGenerator, are_strokes_linked


def test_intersect():
    assert do_intersect(-1, -1, 1, 1, 1, 1, -1, -1)
    assert do_intersect(-1, -1, -1, 1, -1, 1, 1, 1)
    assert not do_intersect(-1, -1, -1, 1, 1, -1, 1, 1)
    assert not do_intersect(-1, 1, 0, 0, 0, -1, 1, 0)


def test_are_strokes_linked():
    assert are_strokes_linked(strokes=[0], intersection_matrix=[[1]])
    assert are_strokes_linked(strokes=[0, 1], intersection_matrix=[[1, 1], [1, 1]])
    assert not are_strokes_linked(strokes=[0, 1], intersection_matrix=[[1, 0], [0, 1]])
    assert not are_strokes_linked(
        strokes=[0, 1, 2, 3], intersection_matrix=[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    )
    assert not are_strokes_linked(
        strokes=[0, 3], intersection_matrix=[[1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 1], [0, 1, 1, 1]]
    )


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
