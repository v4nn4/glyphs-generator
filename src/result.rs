use crate::Glyph;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GenerationResult {
    pub glyphs: std::collections::HashMap<usize, Vec<Glyph>>,
    pub report: Vec<u8>,
}

impl GenerationResult {
    pub fn new(glyphs: std::collections::HashMap<usize, Vec<Glyph>>, report: Vec<u8>) -> Self {
        Self { glyphs, report }
    }
}
