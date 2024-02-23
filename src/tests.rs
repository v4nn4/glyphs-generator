use crate::Coordinate;
use crate::GlyphGenerator;
use crate::Stroke;

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

    let alphabet = GlyphGenerator::generate(strokes);
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
