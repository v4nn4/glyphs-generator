from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Coordinate:
    x: float
    y: float

    def rot90(self) -> "Coordinate":
        angle = np.pi / 2  # 90 degrees in radians
        rotation_matrix = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )
        rotated_point = np.dot(rotation_matrix, np.array([self.x, self.y]))
        return Coordinate(x=rotated_point[0], y=rotated_point[1])

    def flip_left(self) -> "Coordinate":
        return Coordinate(x=self.x, y=-self.y)

    def flip_up(self) -> "Coordinate":
        return Coordinate(x=-self.x, y=self.y)


@dataclass
class Stroke:
    start: Coordinate
    end: Coordinate

    def __repr__(self) -> str:
        return f"({self.start.x}, {self.start.y})-({self.end.x}, {self.end.y})"


@dataclass
class Glyph:
    strokes: List[Stroke]

    def _apply_coordinate_transformation(
        self, transformation: Callable[[Coordinate], Coordinate]
    ) -> "Glyph":
        rotated_strokes = []
        for stroke in self.strokes:
            start = transformation(stroke.start)
            end = transformation(stroke.end)
            rotated_stroke = Stroke(start=start, end=end)
            rotated_strokes.append(rotated_stroke)
        return Glyph(strokes=rotated_strokes)

    def rot90(self) -> "Glyph":
        return self._apply_coordinate_transformation(lambda x: x.rot90())

    def flip_left(self) -> "Glyph":
        return self._apply_coordinate_transformation(lambda x: x.flip_left())

    def flip_up(self) -> "Glyph":
        return self._apply_coordinate_transformation(lambda x: x.flip_up())

    def __eq__(self, other: "Glyph") -> bool:
        return np.abs(self.rasterize(5) - other.rasterize(5)).sum() == 0

    def rasterize(self, dimension: int) -> np.ndarray:
        array = np.zeros(shape=(dimension, dimension))

        def world_to_view(coordinate: Coordinate) -> Tuple[int, int]:
            return int(
                np.round(coordinate.x * (dimension - 1) / 2 + (dimension - 1) / 2)
            ), int(np.round(coordinate.y * (dimension - 1) / 2 + (dimension - 1) / 2))

        for stroke in self.strokes:
            x0, y0 = world_to_view(stroke.start)
            x1, y1 = world_to_view(stroke.end)
            array[x0, y0] = 1
            array[x1, y1] = 1
            if x0 == x1:
                for y in range(min(y0, y1), min(max(y0, y1) + 1, dimension)):
                    array[x0, y] = 1
            elif y0 == y1:
                for x in range(min(x0, x1), min(max(x0, x1) + 1, dimension)):
                    array[x, y0] = 1
            else:
                raise Exception("Slope is not implemented")
        return array

    def intersect(self, stroke: Stroke) -> bool:
        return (
            np.multiply(self.rasterize(5), Glyph(strokes=[stroke]).rasterize(5)).sum()
            != 0
        )

    def plot(self) -> plt.Figure:
        import matplotlib.pyplot as plt
        import matplotlib.lines as lines

        fig = plt.figure(figsize=(3, 3))
        for stroke in self.strokes:
            fig.add_artist(
                lines.Line2D(
                    [(1 + stroke.start.x) / 2, (1 + stroke.end.x) / 2],
                    [(1 + stroke.start.y) / 2, (1 + stroke.end.y) / 2],
                    linewidth=50,
                    color="black",
                )
            )
        return fig


@dataclass
class Alphabet:
    glyphs: Dict[int, List[Glyph]]

    def rasterize(self, dimension: int = 5, margin: int = 1) -> np.ndarray:
        largest_number_of_glyphs_per_order = np.max(
            np.array([len(glyphs) for glyphs in self.glyphs.values()])
        )
        strokes = self.glyphs[len(self.glyphs) - 1][0].strokes
        tensor = np.zeros(
            shape=(
                (dimension + margin) * len(strokes),
                (dimension + margin) * largest_number_of_glyphs_per_order,
            )
        )
        for order, glyphs in self.glyphs.items():
            for i, glyph in enumerate(glyphs):
                tensor[
                    (dimension + margin) * order : (dimension + margin) * order
                    + dimension,
                    (dimension + margin) * i : (dimension + margin) * i + dimension,
                ] = glyph.rasterize(dimension)
        return tensor
