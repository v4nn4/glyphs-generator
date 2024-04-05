def test_flip_horizontal(basic_generator):
    generator = basic_generator
    (th, lv, d1, d2, rv, bh) = [generator.to_internal(x) for x in generator.parent_strokes]

    for stroke in [th, lv, rv, bh]:
        assert stroke in generator.transform(th)

    for stroke in [d1, d2]:
        assert stroke in generator.transform(d1)

    assert (rv | th | d1) in generator.transform(lv | bh | d1)
