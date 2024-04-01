from typing import List
from dataclasses import dataclass


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


@dataclass()
class InternalGlyph:
    strokes: List[InternalStroke]
    identifier: int

    def __eq__(self, __value: "InternalGlyph") -> bool:
        return self.identifier == __value.identifier  # faster eq

    def __hash__(self) -> int:
        return self.identifier  # faster hash

    def __or__(self, __value: "InternalGlyph") -> "InternalGlyph":
        return InternalGlyph(
            strokes=list(set(self.strokes + __value.strokes)),
            identifier=self.identifier | __value.identifier,
        )
