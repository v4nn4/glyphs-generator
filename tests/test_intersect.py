from glyphs_generator import do_intersect


def test_intersect():
    assert do_intersect(-1, -1, 1, 1, 1, 1, -1, -1)
    assert do_intersect(-1, -1, -1, 1, -1, 1, 1, 1)
    assert not do_intersect(-1, -1, -1, 1, 1, -1, 1, 1)
