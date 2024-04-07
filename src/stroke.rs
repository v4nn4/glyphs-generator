use serde::{Deserialize, Serialize};
use std::hash::{Hash, Hasher};

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub struct Stroke {
    pub x0: f64,
    pub y0: f64,
    pub x1: f64,
    pub y1: f64,
}

impl Stroke {
    pub fn is_inverse(&self, other: &Stroke) -> bool {
        self.x0 == other.x1 && self.y0 == other.y1 && self.x1 == other.x0 && self.y1 == other.y0
    }
}

impl PartialEq for Stroke {
    fn eq(&self, other: &Self) -> bool {
        const TOLERANCE: f64 = 1e-16; // Define a suitable tolerance

        (self.x0 - other.x0).abs() < TOLERANCE
            && (self.y0 - other.y0).abs() < TOLERANCE
            && (self.x1 - other.x1).abs() < TOLERANCE
            && (self.y1 - other.y1).abs() < TOLERANCE
    }
}

impl Eq for Stroke {}

impl Hash for Stroke {
    fn hash<H: Hasher>(&self, state: &mut H) {
        const SCALE: f64 = 1e16; // Scale factor for discretization

        // Discretize or round the f64 fields
        let x0 = (self.x0 * SCALE).round() as i64;
        let y0 = (self.y0 * SCALE).round() as i64;
        let x1 = (self.x1 * SCALE).round() as i64;
        let y1 = (self.y1 * SCALE).round() as i64;

        // Hash the discretized values
        x0.hash(state);
        y0.hash(state);
        x1.hash(state);
        y1.hash(state);
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct InternalStroke {
    pub index: usize,
}
