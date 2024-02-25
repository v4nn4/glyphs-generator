use serde::{Deserialize, Serialize};

const EPSILON: f64 = 1.0e-10;

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
        Coordinate::new(-self.y, self.x)
    }

    pub fn flip_left(&self) -> Self {
        Coordinate::new(-self.x, self.y)
    }

    pub fn flip_up(&self) -> Self {
        Coordinate::new(self.x, -self.y)
    }
}

impl PartialEq for Coordinate {
    fn eq(&self, other: &Self) -> bool {
        ((self.x - other.x).abs() < EPSILON) && ((self.y - other.y).abs() < EPSILON)
    }
}
