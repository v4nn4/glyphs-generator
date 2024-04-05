import pytest

from glyphs_generator.data import Point
from glyphs_generator.build import build_generator


@pytest.fixture(scope="module")
def basic_generator():
    anchor_points = [
        Point(-1, -1),
        Point(-1, 1),
        Point(1, -1),
        Point(1, 1),
    ]
    return build_generator(anchor_points)


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
    return build_generator(anchor_points)
