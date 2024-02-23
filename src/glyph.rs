use ndarray::arr2;
use serde::{Deserialize, Serialize};
use std::f64::consts::PI;

#[derive(Serialize, Deserialize, Debug, Clone, Copy)]
pub struct Coordinate {
    pub x: f64,
    pub y: f64,
}

impl Coordinate {
    pub fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    pub fn rot90(&self) -> Self {
        let angle = PI / 2.0; // 90 degrees in radians
        let rotation_matrix = arr2(&[[angle.cos(), -angle.sin()], [angle.sin(), angle.cos()]]);
        let point = arr2(&[[self.x], [self.y]]);
        let rotated_point = rotation_matrix.dot(&point);
        Coordinate::new(rotated_point[[0, 0]], rotated_point[[1, 0]])
    }

    pub fn flip_left(&self) -> Self {
        Coordinate::new(self.x, -self.y)
    }

    pub fn flip_up(&self) -> Self {
        Coordinate::new(-self.x, self.y)
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Stroke {
    pub start: Coordinate,
    pub end: Coordinate,
}

impl Stroke {
    pub fn new(start: Coordinate, end: Coordinate) -> Self {
        Self { start, end }
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Glyph {
    pub strokes: Vec<Stroke>,
}

impl Glyph {
    pub fn new(strokes: Vec<Stroke>) -> Self {
        Self { strokes }
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

        Self {
            strokes: rotated_strokes,
        }
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

    pub fn rasterize(&self, glyph_size: usize) -> Vec<Vec<u8>> {
        let mut array = vec![vec![0u8; glyph_size]; glyph_size];

        let world_to_view = |coordinate: &Coordinate| -> (usize, usize) {
            (
                ((coordinate.x * (glyph_size as f64 - 1.0) / 2.0 + (glyph_size as f64 - 1.0) / 2.0)
                    .round() as usize)
                    .min(glyph_size - 1),
                ((coordinate.y * (glyph_size as f64 - 1.0) / 2.0 + (glyph_size as f64 - 1.0) / 2.0)
                    .round() as usize)
                    .min(glyph_size - 1),
            )
        };

        for stroke in &self.strokes {
            let (x0, y0) = world_to_view(&stroke.start);
            let (x1, y1) = world_to_view(&stroke.end);
            array[y0][x0] = 1;
            array[y1][x1] = 1;

            if x0 == x1 {
                for y in
                    std::cmp::min(y0, y1)..=std::cmp::min(std::cmp::max(y0, y1), glyph_size - 1)
                {
                    array[y][x0] = 1;
                }
            } else if y0 == y1 {
                for x in
                    std::cmp::min(x0, x1)..=std::cmp::min(std::cmp::max(x0, x1), glyph_size - 1)
                {
                    array[y0][x] = 1;
                }
            } else {
                let slope = (x1 as f64 - x0 as f64) / (y1 as f64 - y0 as f64);
                for y in
                    std::cmp::min(y0, y1)..=std::cmp::min(std::cmp::max(y0, y1), glyph_size - 1)
                {
                    let x = ((slope * (y as f64 - y0 as f64) + x0 as f64).floor() as usize)
                        .min(glyph_size - 1);
                    array[y][x] = 1;
                }
            }
        }
        array
    }

    pub fn intersect(&self, stroke: &Stroke, glyph_size: usize) -> bool {
        let self_raster = self.rasterize(glyph_size);
        let stroke_glyph = Glyph {
            strokes: vec![stroke.clone()],
        };
        let stroke_raster = stroke_glyph.rasterize(glyph_size);

        for y in 0..glyph_size {
            for x in 0..glyph_size {
                // Check if both cells are occupied
                if self_raster[y][x] == 1 && stroke_raster[y][x] == 1 {
                    return true;
                }
            }
        }

        false
    }
}

impl PartialEq for Glyph {
    fn eq(&self, other: &Self) -> bool {
        let size = 7; // Fixed size for rasterization as per the Python example
        let self_raster = self.rasterize(size);
        let other_raster = other.rasterize(size);

        // Compare the two rasterized forms element by element
        for (row_self, row_other) in self_raster.iter().zip(other_raster.iter()) {
            for (val_self, val_other) in row_self.iter().zip(row_other.iter()) {
                if val_self != val_other {
                    return false; // Found a mismatch, the glyphs are not equal
                }
            }
        }

        true // No mismatches found, the glyphs are equal
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Alphabet {
    pub glyphs: std::collections::HashMap<usize, Vec<Glyph>>,
}

impl Alphabet {
    pub fn new(glyphs: std::collections::HashMap<usize, Vec<Glyph>>) -> Self {
        Self { glyphs }
    }

    // Placeholder for the rasterize function
    // Details omitted for brevity
}
