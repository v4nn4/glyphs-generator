from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
import torch


class GlyphGenerator:
    def __init__(self, strokes: np.ndarray):
        self._N = len(strokes[0])
        self._S = len(strokes)
        self._strokes = strokes

    @staticmethod
    def _is_equal(glyph_1: np.ndarray, glyph_2: np.ndarray) -> bool:
        return (
            np.array_equal(glyph_1, glyph_2)
            or np.array_equal(glyph_1.T, glyph_2)
            or np.array_equal(np.fliplr(glyph_1), glyph_2)
            or np.array_equal(np.flipud(glyph_1), glyph_2)
            or np.array_equal(np.fliplr(glyph_1.T), glyph_2)
            or np.array_equal(np.flipud(glyph_1.T), glyph_2)
            or np.array_equal(np.fliplr(glyph_1).T, glyph_2)
            or np.array_equal(np.flipud(glyph_1).T, glyph_2)
        )

    @staticmethod
    def _is_eligible(glyph: np.ndarray) -> bool:
        N = len(glyph)
        max = torch.max(
            torch.nn.AdaptiveAvgPool2d(N - 1)(
                torch.tensor(glyph, dtype=torch.float32).view(1, 1, N, N)
            )
        ).item()
        return max

    def generate(self):
        strokes = self._strokes
        glyphs = {i: [] for i in np.arange(0, len(strokes))}
        glyphs[0].append(strokes[0])  # assuming glyphs are all same up to rotation
        # for stroke in strokes:
        #    if all(not is_equal(stroke, chosen_stroke) for chosen_stroke in stored_glyphs[0]):
        #        stored_glyphs[0].append(stroke)
        for order in np.arange(0, len(glyphs)):
            for chosen_stroke in glyphs[order]:
                for stroke in strokes:
                    all_glyphs = reduce(list.__add__, glyphs.values())
                    if np.multiply(chosen_stroke, stroke).sum() == 0:
                        continue
                    glyph = np.clip(chosen_stroke + stroke, 0, 255)
                    if self._is_eligible(glyph):
                        if all(
                            [
                                not self._is_equal(glyph, stored_glyph)
                                for stored_glyph in all_glyphs
                            ]
                        ):
                            glyphs[order + 1].append(glyph)
        return glyphs

    def plot(self):
        glyphs = self.generate()
        N = self._N
        S = self._S
        max_glypgs_per_order = np.max([len(glyphs) for _, glyphs in glyphs.items()])
        canvas = np.zeros(shape=((N + 1) * S + 1, (N + 1) * max_glypgs_per_order + 1))

        for order, glyphs in glyphs.items():
            i = 0
            for glyph in glyphs:
                canvas[
                    1 + (N + 1) * order : 1 + (N + 1) * (order + 1) - 1,
                    1 + (N + 1) * i : 1 + (N + 1) * (i + 1) - 1,
                ] = glyph
                i += 1
        plt.imshow(255 - np.array(canvas) * 255, cmap="gray")
        plt.axis("off")
        plt.tight_layout()
