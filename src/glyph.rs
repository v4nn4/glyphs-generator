use crate::rasterize::rasterize;
use crate::Coordinate;
use crate::Stroke;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Glyph {
    pub strokes: Vec<Stroke>,
    raster: Vec<Vec<u8>>,
    dimension: usize,
}

impl Glyph {
    pub fn new(strokes: &Vec<Stroke>, dimension: usize) -> Self {
        Self {
            strokes: strokes.to_vec(),
            raster: rasterize(strokes, dimension),
            dimension: dimension,
        }
    }

    fn apply_coordinate_transformation<F>(&self, transformation: F) -> Self
    where
        F: Fn(&Coordinate) -> Coordinate,
    {
        let rotated_strokes = self
            .strokes
            .iter()
            .map(|stroke| {
                let start = transformation(&stroke.start);
                let end = transformation(&stroke.end);
                Stroke { start, end }
            })
            .collect();

        Self::new(&rotated_strokes, self.dimension)
    }

    pub fn rot90(&self) -> Self {
        self.apply_coordinate_transformation(|coord| coord.rot90())
    }

    pub fn flip_left(&self) -> Self {
        self.apply_coordinate_transformation(|coord| coord.flip_left())
    }

    pub fn flip_up(&self) -> Self {
        self.apply_coordinate_transformation(|coord| coord.flip_up())
    }

    pub fn intersect(&self, stroke: &Stroke, dimension: usize) -> bool {
        let raster = &self.raster;
        let stroke_raster = rasterize(&vec![stroke.clone()], dimension);

        for y in 0..dimension {
            for x in 0..dimension {
                if raster[y][x] == 1 && stroke_raster[y][x] == 1 {
                    return true;
                }
            }
        }

        false
    }

    pub fn contains_stroke(&self, stroke: &Stroke) -> bool {
        self.strokes.iter().any(|s| s == stroke)
    }
}

impl PartialEq for Glyph {
    fn eq(&self, other: &Self) -> bool {
        let raster = &self.raster;
        let other_raster = &other.raster;

        for (row_self, row_other) in raster.iter().zip(other_raster.iter()) {
            for (val_self, val_other) in row_self.iter().zip(row_other.iter()) {
                if val_self != val_other {
                    return false;
                }
            }
        }

        true
    }
}
