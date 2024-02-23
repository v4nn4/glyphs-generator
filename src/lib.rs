mod generator;
mod glyph;

#[cfg(test)]
mod tests;

pub use generator::GlyphGenerator;
pub use glyph::Alphabet;
pub use glyph::Coordinate;
pub use glyph::Glyph;
pub use glyph::Stroke;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn run(data: String) -> String {
    let strokes: Vec<Stroke> = serde_json::from_str(&data).expect("Error deserializing JSON");
    let alphabet = GlyphGenerator::generate(strokes);
    serde_json::to_string(&alphabet).unwrap()
}
