use crate::{GenerationResult, Glyph, Stroke};
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

    pub fn generate(strokes: &Vec<Stroke>, dimension: usize) -> GenerationResult {
        let mut result: HashMap<usize, Vec<Glyph>> = HashMap::new();
        for k in 0..strokes.len() {
            result.insert(k, Vec::new());
        }
        result
            .get_mut(&0)
            .unwrap()
            .push(Glyph::new(&vec![strokes[0].clone()]));
        let mut report: Vec<u8> = vec![0, 0, 0];
        for order in 0..strokes.len() {
            if order == strokes.len() - 1 {
                continue;
            }
            let mut observed: Vec<Glyph> = Vec::new();
            if let Some(glyphs) = result.get(&order).cloned() {
                for glyph in glyphs {
                    let mutable_glyph = glyph.clone();
                    let filtered_strokes = strokes.iter().filter(|s| !glyph.contains_stroke(s));
                    for stroke in filtered_strokes {
                        if !mutable_glyph.intersect(stroke, dimension) {
                            report[1] += 1;
                            continue;
                        }

                        let mut new_strokes = glyph.strokes.clone();
                        new_strokes.push(stroke.clone());
                        let next_glyph = Glyph::new(&new_strokes);

                        if observed.contains(&next_glyph) {
                            report[2] += 1;
                            continue;
                        } else {
                            observed.push(next_glyph.clone());
                        }

                        report[0] += 1;
                        let all_glyphs = result
                            .values()
                            .flat_map(|v| v.iter())
                            .cloned()
                            .collect::<Vec<Glyph>>();
                        if all_glyphs
                            .iter()
                            .all(|g| !GlyphGenerator::are_equivalent(&next_glyph, g))
                        {
                            result
                                .entry(order + 1)
                                .or_insert_with(Vec::new)
                                .push(next_glyph);
                        }
                    }
                }
            }
        }

        GenerationResult::new(result, report)
    }
}
