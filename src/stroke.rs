use crate::Coordinate;
use serde::{Deserialize, Serialize};

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

impl PartialEq for Stroke {
    fn eq(&self, other: &Self) -> bool {
        self.start == other.start && self.end == other.end
            || self.end == other.start && self.start == other.end
    }
}
