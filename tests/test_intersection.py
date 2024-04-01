def test_intersection(generator):
    (th, lv, d1, d2, rv, bh) = [
        generator.to_internal(x) for x in generator.parent_strokes
    ]
    assert not generator.are_strokes_intersecting(th | bh)
    assert not generator.are_strokes_intersecting(lv | rv)
    assert generator.are_strokes_intersecting(d1 | d2)
    assert generator.are_strokes_intersecting(lv | d1)
    assert generator.are_strokes_intersecting(bh | d2)
    assert generator.are_strokes_intersecting(rv | th)
    assert generator.are_strokes_intersecting(th | lv | d1 | d2 | rv | bh)
