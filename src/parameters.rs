use crate::stroke::Stroke;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Parameters {
    pub parent_strokes: Vec<Stroke>,
    pub intersection_matrix: Vec<Vec<u8>>,
    pub transformation_matrix: Vec<Vec<usize>>,
}
