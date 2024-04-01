import pytest

from glyphs_generator.data import Point
from glyphs_generator.builder import build_generator


@pytest.fixture(scope="module")
def generator():
    anchor_points = [Point(-1, -1), Point(-1, 1), Point(1, -1), Point(1, 1)]
    return build_generator(anchor_points)
