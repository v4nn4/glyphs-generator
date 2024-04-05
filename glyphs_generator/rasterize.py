from typing import List, Tuple
import numpy as np

from .data import Glyph


def world_to_view(x: float, y: float, glyph_size: int) -> Tuple[int, int]:
    return int(np.round(x * (glyph_size - 1) / 2 + (glyph_size - 1) / 2)), int(
        np.round(y * (glyph_size - 1) / 2 + (glyph_size - 1) / 2)
    )


def rasterize(glyph: Glyph, glyph_size: int) -> np.ndarray:
    array = np.zeros(shape=(glyph_size, glyph_size))

    for stroke in glyph.strokes:
        x0, y0 = world_to_view(x=stroke.x0, y=stroke.y0, glyph_size=glyph_size)
        x1, y1 = world_to_view(x=stroke.x1, y=stroke.y1, glyph_size=glyph_size)
        array[y0, x0] = 1
        array[y1, x1] = 1
        if x0 == x1:
            for y in range(min(y0, y1), min(max(y0, y1) + 1, glyph_size)):
                array[y, x0] = 1
        elif y0 == y1:
            for x in range(min(x0, x1), min(max(x0, x1) + 1, glyph_size)):
                array[y0, x] = 1
        else:
            slope = (x1 - x0) / (y1 - y0)
            for y in range(min(y0, y1), min(max(y0, y1) + 1, glyph_size)):
                x = int(np.floor(slope * (y - y0) + x0))
                array[y, x] = 1
    return array


def rasterize_all(
    glyphs: List[Glyph], glyph_size: int = 5, margin: int = 1, nb_glyphs_per_row: int = 6, sort: bool = False
) -> np.ndarray:
    if not sort:
        nb_glyphs = len(glyphs)
        nb_glyphs_per_columns = int(np.ceil(nb_glyphs / nb_glyphs_per_row))
        tensor = np.zeros(
            shape=(
                (glyph_size + margin) * nb_glyphs_per_columns,
                (glyph_size + margin) * nb_glyphs_per_row,
            )
        )
        for k, glyph in enumerate(glyphs):
            j = k % nb_glyphs_per_row
            i = k // nb_glyphs_per_row
            tensor[
                (glyph_size + margin) * i : (glyph_size + margin) * i + glyph_size,
                (glyph_size + margin) * j : (glyph_size + margin) * j + glyph_size,
            ] = rasterize(glyph=glyph, glyph_size=glyph_size)
        return tensor
    else:
        alphabet = {}
        for glyph in glyphs:
            nb_strokes = len(glyph.strokes)
            if (nb_strokes - 1) not in alphabet:
                alphabet[nb_strokes - 1] = []
            alphabet[nb_strokes - 1].append(glyph)
        largest_number_of_glyphs_per_order = np.max(np.array([len(glyphs) for glyphs in alphabet.values()]))
        strokes = alphabet[len(alphabet) - 1][0].strokes
        tensor = np.zeros(
            shape=(
                (glyph_size + margin) * len(strokes),
                (glyph_size + margin) * largest_number_of_glyphs_per_order,
            )
        )
        for order, glyphs in alphabet.items():
            for i, glyph in enumerate(glyphs):
                tensor[
                    (glyph_size + margin) * order : (glyph_size + margin) * order + glyph_size,
                    (glyph_size + margin) * i : (glyph_size + margin) * i + glyph_size,
                ] = rasterize(glyph=glyph, glyph_size=glyph_size)
        return tensor
