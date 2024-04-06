from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True, repr=True)
class Stroke:
    x0: float
    y0: float
    x1: float
    y1: float


@dataclass(frozen=True)
class Glyph:
    strokes: List[Stroke]


@dataclass(frozen=True)
class InternalStroke:
    index: int

    def __eq__(self, __value: "InternalStroke") -> bool:
        return self.index == __value.index

    def __hash__(self) -> int:
        return self.index


@dataclass()
class InternalGlyph:
    strokes: List[InternalStroke]
    identifier: int

    def __eq__(self, __value: "InternalGlyph") -> bool:
        return self.identifier == __value.identifier  # fast eq

    def __or__(self, __value: "InternalGlyph") -> "InternalGlyph":
        indices = [s.index for s in self.strokes] + [s.index for s in __value.strokes]
        indices = list(set(indices))
        return InternalGlyph(
            strokes=[InternalStroke(index=index) for index in indices],
            identifier=self.identifier | __value.identifier,
        )

    @staticmethod
    def empty() -> "InternalGlyph":
        return InternalGlyph(strokes=[], identifier=0)

    @staticmethod
    def from_stroke(stroke: InternalStroke) -> "InternalGlyph":
        return InternalGlyph(strokes=[stroke], identifier=2**stroke.index)
