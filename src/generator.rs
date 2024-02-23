use crate::{Alphabet, Glyph, Stroke};
use std::collections::HashMap;

pub struct GlyphGenerator;

impl GlyphGenerator {
    pub fn are_equivalent(glyph_1: &Glyph, glyph_2: &Glyph) -> bool {
        let glyph_1_rot90 = glyph_1.rot90();
        let glyph_1_rot180 = glyph_1_rot90.rot90();
        let glyph_1_rot270 = glyph_1_rot180.rot90();

        glyph_1 == glyph_2
            || &glyph_1_rot90 == glyph_2
            || &glyph_1_rot180 == glyph_2
            || &glyph_1_rot270 == glyph_2
            || &glyph_1.flip_left() == glyph_2
            || &glyph_1_rot90.flip_left() == glyph_2
            || &glyph_1_rot180.flip_left() == glyph_2
            || &glyph_1_rot270.flip_left() == glyph_2
            || &glyph_1.flip_up() == glyph_2
            || &glyph_1_rot90.flip_up() == glyph_2
            || &glyph_1_rot180.flip_up() == glyph_2
            || &glyph_1_rot270.flip_up() == glyph_2
    }

    pub fn generate(strokes: Vec<Stroke>) -> Alphabet {
        let mut alphabet: HashMap<usize, Vec<Glyph>> = HashMap::new();
        for k in 0..strokes.len() {
            alphabet.insert(k, Vec::new());
        }
        alphabet
            .get_mut(&0)
            .unwrap()
            .push(Glyph::new(vec![strokes[0].clone()]));
        for order in 0..strokes.len() {
            if order == strokes.len() - 1 {
                continue;
            }
            if let Some(glyphs) = alphabet.get(&order).cloned() {
                for glyph in glyphs {
                    for stroke in &strokes {
                        if !glyph.intersect(stroke, 7) {
                            continue;
                        }

                        let mut new_strokes = glyph.strokes.clone();
                        new_strokes.push(stroke.clone());
                        let next_glyph = Glyph::new(new_strokes);

                        let all_glyphs = alphabet
                            .values()
                            .flat_map(|v| v.iter())
                            .cloned()
                            .collect::<Vec<Glyph>>();
                        if all_glyphs
                            .iter()
                            .all(|g| !GlyphGenerator::are_equivalent(&next_glyph, g))
                        {
                            alphabet
                                .entry(order + 1)
                                .or_insert_with(Vec::new)
                                .push(next_glyph);
                        }
                    }
                }
            }
        }

        Alphabet::new(alphabet)
    }
}
