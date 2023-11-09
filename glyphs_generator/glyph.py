from dataclasses import dataclass
from functools import reduce
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

    def rasterize(self, glyph_size: int) -> np.ndarray:
        array = np.zeros(shape=(glyph_size, glyph_size))

        def world_to_view(coordinate: Coordinate) -> Tuple[int, int]:
            return int(
                np.round(coordinate.x * (glyph_size - 1) / 2 + (glyph_size - 1) / 2)
            ), int(np.round(coordinate.y * (glyph_size - 1) / 2 + (glyph_size - 1) / 2))

        for stroke in self.strokes:
            x0, y0 = world_to_view(stroke.start)
            x1, y1 = world_to_view(stroke.end)
            array[x0, y0] = 1
            array[x1, y1] = 1
            if x0 == x1:
                for y in range(min(y0, y1), min(max(y0, y1) + 1, glyph_size)):
                    array[x0, y] = 1
            elif y0 == y1:
                for x in range(min(x0, x1), min(max(x0, x1) + 1, glyph_size)):
                    array[x, y0] = 1
            else:
                slope = (y1 - y0) / (x1 - x0)
                for x in range(min(x0, x1), min(max(x0, x1) + 1, glyph_size)):
                    y = int(np.floor(slope * (x - x0) + y0))
                    array[x, y] = 1
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

    def rasterize(
        self,
        glyph_size: int = 5,
        margin: int = 1,
        sorted: bool = True,
        nb_glyphs_per_row: int = 5,
    ) -> np.ndarray:
        if sorted:
            largest_number_of_glyphs_per_order = np.max(
                np.array([len(glyphs) for glyphs in self.glyphs.values()])
            )
            strokes = self.glyphs[len(self.glyphs) - 1][0].strokes
            tensor = np.zeros(
                shape=(
                    (glyph_size + margin) * len(strokes),
                    (glyph_size + margin) * largest_number_of_glyphs_per_order,
                )
            )
            for order, glyphs in self.glyphs.items():
                for i, glyph in enumerate(glyphs):
                    tensor[
                        (glyph_size + margin) * order : (glyph_size + margin) * order
                        + glyph_size,
                        (glyph_size + margin) * i : (glyph_size + margin) * i
                        + glyph_size,
                    ] = glyph.rasterize(glyph_size)
        else:
            nb_glyphs = np.array([len(glyphs) for glyphs in self.glyphs.values()]).sum()
            nb_glyphs_per_columns = int(np.ceil(nb_glyphs / nb_glyphs_per_row))
            strokes = self.glyphs[len(self.glyphs) - 1][0].strokes
            tensor = np.zeros(
                shape=(
                    (glyph_size + margin) * nb_glyphs_per_columns,
                    (glyph_size + margin) * nb_glyphs_per_row,
                )
            )
            all_glyphs = reduce(list.__add__, self.glyphs.values())
            for k, glyph in enumerate(all_glyphs):
                j = k % nb_glyphs_per_row
                i = k // nb_glyphs_per_row
                tensor[
                    (glyph_size + margin) * i : (glyph_size + margin) * i + glyph_size,
                    (glyph_size + margin) * j : (glyph_size + margin) * j + glyph_size,
                ] = glyph.rasterize(glyph_size)
        return tensor
