mod coordinate;
mod generator;
mod glyph;
mod rasterize;
mod result;
mod stroke;

#[cfg(test)]
mod tests;

pub use coordinate::Coordinate;
pub use generator::GlyphGenerator;
pub use glyph::Glyph;
pub use result::GenerationResult;
use serde::{Deserialize, Serialize};
pub use stroke::Stroke;
use wasm_bindgen::prelude::*;

#[derive(Serialize, Deserialize)]
pub struct Computable {
    strokes: Vec<Stroke>,
    pixel_dimension: usize,
}

#[wasm_bindgen]
pub fn run(input: String) -> String {
    let computable: Computable = serde_json::from_str(&input).expect("Error deserializing JSON");
    let strokes = computable.strokes;
    let result = GlyphGenerator::generate(&strokes, computable.pixel_dimension);
    serde_json::to_string(&result).unwrap()
}
