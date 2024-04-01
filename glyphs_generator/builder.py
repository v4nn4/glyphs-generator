from typing import List, Tuple

from .data import Point, Stroke
from .generator import GlyphGenerator


def _build_strokes(points: List[Point]) -> List[Tuple[Stroke, Tuple[int, int]]]:
    strokes = []
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            if point1 != point2:
                stroke = Stroke(x0=point1.x, y0=point1.y, x1=point2.x, y1=point2.y)
                reversed_stroke = Stroke(
                    x0=point2.x, y0=point2.y, x1=point1.x, y1=point1.y
                )
                list_strokes = [stroke for (stroke, _) in strokes]
                if stroke not in list_strokes and reversed_stroke not in list_strokes:
                    strokes.append((stroke, (i, j)))
    return strokes


# def _build_stroke_to_point_mapping(nb_points: int) -> Dict[int, Tuple[int, int]]:
#    stroke_to_point_mapping = {}
#    visited_pairs = []
#    i = 0
#    for p1 in range(nb_points):
#        for p2 in range(nb_points):
#            if p1 != p2:
#                key = f"{p1}_{p2}"
#                reversed_key = f"{p2}_{p1}"
#                if key not in visited_pairs and reversed_key not in visited_pairs:
#                    stroke_to_point_mapping[i] = (p1, p2)
#                    visited_pairs.append(key)
#                    i += 1
#    return stroke_to_point_mapping


def _build_transformation_matrix(points: List[Point]) -> List[List[int]]:
    p = len(points)

    def fv(point):
        return Point(x=point.x, y=-point.y)

    def fh(point):
        return Point(x=-point.x, y=point.y)

    def r(point):
        return Point(x=point.y, y=point.x)

    fns = {"fv": fv, "fh": fh, "r": r}

    def get_point_index(point: Point) -> int:
        for i, point_ in enumerate(points):
            if point.x == point_.x and point.y == point_.y:
                return i
        raise Exception(f"Point not found for coordinates ({point.x}, {point.y})")

    point_transformation_table = {
        k: {i: get_point_index(fn(point)) for (i, point) in enumerate(points)}
        for (k, fn) in fns.items()
    }

    fv = point_transformation_table["fv"]
    fh = point_transformation_table["fh"]
    r = point_transformation_table["r"]
    point_transformation_table["fvr"] = {k: fv[r[k]] for k in range(p)}
    point_transformation_table["fhr"] = {k: fh[r[k]] for k in range(p)}
    point_transformation_table["r2"] = {k: r[r[k]] for k in range(p)}
    point_transformation_table["r3"] = {k: r[r[r[k]]] for k in range(p)}

    strokes = _build_strokes(points)

    def find_stroke(p1: int, p2: int) -> int:
        for stroke_index, (_, (p1_, p2_)) in enumerate(strokes):
            if p1 == p1_ and p2 == p2_ or p1 == p2_ and p2 == p1_:
                return stroke_index
        raise Exception(f"Stroke not found for coordinates ({p1}, {p2})")

    transformation_table = [
        [_ for _ in point_transformation_table.keys()] for _ in strokes
    ]
    for i, (_, (p1, p2)) in enumerate(strokes):
        for j, fn in enumerate(point_transformation_table.values()):
            transformation_table[i][j] = find_stroke(fn[p1], fn[p2])

    return transformation_table


def _build_intersection_matrix():
    adjacency_matrix = [
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
    ]
    return adjacency_matrix


def build_generator(anchor_points: List[Point]) -> GlyphGenerator:
    parent_strokes = [stroke for (stroke, _) in _build_strokes(anchor_points)]
    intersection_matrix = _build_intersection_matrix()
    transformation_matrix = _build_transformation_matrix(anchor_points)

    return GlyphGenerator(
        parent_strokes=parent_strokes,
        intersection_matrix=intersection_matrix,
        transformation_matrix=transformation_matrix,
    )
