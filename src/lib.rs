mod generator;
mod glyph;

#[cfg(test)]
mod tests;

pub use generator::GlyphGenerator;
pub use glyph::Alphabet;
pub use glyph::Coordinate;
pub use glyph::Glyph;
pub use glyph::Stroke;
use serde::{Deserialize, Serialize};
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
    let alphabet = GlyphGenerator::generate(strokes);
    serde_json::to_string(&alphabet).unwrap()
}
