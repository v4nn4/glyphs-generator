use crate::run;
use crate::Coordinate;
use crate::Glyph;
use crate::GlyphGenerator;
use crate::Stroke;
use std::fs;

#[test]
fn test_are_glyphs_equal() {
    // U-shape
    let strokes1 = vec![
        Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(-1.0, 1.0)),
        Stroke::new(Coordinate::new(1.0, -1.0), Coordinate::new(1.0, 1.0)),
        Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(1.0, -1.0)),
    ];

    // N-shape
    let strokes2 = vec![
        Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(-1.0, 1.0)),
        Stroke::new(Coordinate::new(1.0, -1.0), Coordinate::new(1.0, 1.0)),
        Stroke::new(Coordinate::new(-1.0, 1.0), Coordinate::new(1.0, 1.0)),
    ];

    let glyph1 = Glyph::new(&strokes1, 9);
    let glyph2 = Glyph::new(&strokes2, 9);
    assert!(glyph1 != glyph2);

    let glyph3 = glyph1.flip_up();
    assert!(glyph3 == glyph2);
}

#[test]
fn test_glyph_intersects_with_stroke() {
    // T-shape
    let stroke1 = Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(-1.0, 1.0));
    let stroke2 = Stroke::new(Coordinate::new(0.0, 0.0), Coordinate::new(-1.0, 0.0));
    let glyph = Glyph::new(&vec![stroke1, stroke2], 9);
    let stroke = Stroke::new(Coordinate::new(1.0, -1.0), Coordinate::new(1.0, 1.0));
    glyph.intersect(&stroke, 9);
}

#[test]
fn generate_creates_correct_number_of_glyphs() {
    let strokes = vec![
        Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(-1.0, 1.0)),
        Stroke::new(Coordinate::new(0.0, -1.0), Coordinate::new(0.0, 1.0)),
        Stroke::new(Coordinate::new(1.0, -1.0), Coordinate::new(1.0, 1.0)),
        Stroke::new(Coordinate::new(-1.0, -1.0), Coordinate::new(1.0, -1.0)),
        Stroke::new(Coordinate::new(-1.0, 0.0), Coordinate::new(1.0, 0.0)),
        Stroke::new(Coordinate::new(-1.0, 1.0), Coordinate::new(1.0, 1.0)),
    ];

    let alphabet = GlyphGenerator::generate(&strokes, 9);
    assert_eq!(alphabet.glyphs.len(), 6);
    let keys_and_expected_lengths = vec![(0, 1), (1, 2), (2, 4), (3, 5), (4, 2), (5, 1)];
    for (key, expected_length) in keys_and_expected_lengths {
        let vec_length = alphabet.glyphs.get(&key).map_or(0, |v| v.len()); // Use 0 if key is not found
        assert_eq!(
            vec_length, expected_length,
            "Mismatch for key {}: expected {}, got {}",
            key, expected_length, vec_length
        );
    }
}

#[test]
fn test_11_strokes() {
    let file_content = fs::read_to_string(
        "/Users/romflorentz/Documents/Repos/glyphs-generator/examples/strokes_11.json",
    )
    .expect("Failed to read file")
    .to_string();
    let output = run(file_content);
    println!("{}", output);
}
