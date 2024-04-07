use crate::glyph::Glyph;
use crate::glyph::InternalGlyph;
use crate::parameters::Parameters;
use crate::stroke::InternalStroke;
use crate::stroke::Stroke;

#[derive(Debug, Clone)]
pub struct GlyphGenerator {
    pub parameters: Parameters,
}

impl GlyphGenerator {
    pub fn new(parameters: Parameters) -> Self {
        Self { parameters }
    }

    pub fn are_strokes_intersecting(&self, glyph: &InternalGlyph) -> bool {
        glyph.strokes.iter().all(|stroke| {
            glyph.strokes.iter().any(|other| {
                stroke.index != other.index
                    && self.parameters.intersection_matrix[stroke.index][other.index] == 1
            })
        })
    }

    pub fn transform(&self, glyph: &InternalGlyph) -> Vec<InternalGlyph> {
        let nb_transformations = self.parameters.transformation_matrix[0].len();
        (0..nb_transformations)
            .map(|i| {
                glyph
                    .strokes
                    .iter()
                    .fold(InternalGlyph::empty(), |acc, stroke| {
                        let stroke_index = self.parameters.transformation_matrix[stroke.index][i];
                        acc.union(&InternalGlyph::from_stroke(InternalStroke {
                            index: stroke_index,
                        }))
                    })
            })
            .collect()
    }

    pub fn to_glyph(&self, glyph: &InternalGlyph) -> Glyph {
        Glyph {
            strokes: glyph
                .strokes
                .iter()
                .map(|s| self.parameters.parent_strokes[s.index].clone())
                .collect(),
        }
    }

    pub fn from_stroke(&self, stroke: &Stroke) -> InternalGlyph {
        self.parameters
            .parent_strokes
            .iter()
            .enumerate()
            .find_map(|(i, parent_stroke)| {
                if stroke == parent_stroke || stroke.is_inverse(parent_stroke) {
                    Some(InternalGlyph::from_stroke(InternalStroke { index: i }))
                } else {
                    None
                }
            })
            .expect("Could not find stroke in parent strokes")
    }

    pub fn generate(&self, strokes: &[Stroke], seed: &Stroke) -> Vec<Glyph> {
        let n = strokes.len();
        let seed_internal = self.from_stroke(seed);
        let strokes_internal: Vec<InternalGlyph> = strokes
            .iter()
            .map(|stroke| self.from_stroke(stroke))
            .collect();

        let mut glyphs: Vec<Vec<InternalGlyph>> = vec![Vec::new(); n];
        glyphs[0].push(seed_internal);

        for i in 0..n - 1 {
            let mut next_glyphs = Vec::new();

            for glyph in &glyphs[i] {
                for stroke in &strokes_internal {
                    let next_glyph = glyph.union(stroke);
                    if next_glyph.strokes.len() < i + 2 {
                        continue;
                    }
                    if next_glyphs.contains(&next_glyph) {
                        continue;
                    }
                    if self.are_strokes_intersecting(&next_glyph) {
                        let transformed_glyphs = self.transform(&next_glyph);
                        if transformed_glyphs
                            .iter()
                            .all(|g| !glyphs[i + 1].contains(&g))
                        {
                            next_glyphs.push(next_glyph);
                        }
                    }
                }
            }

            glyphs[i + 1].extend(next_glyphs);
        }

        // Convert and flatten the glyphs to the desired type
        glyphs
            .into_iter()
            .flatten()
            .map(|g| self.to_glyph(&g))
            .collect()
    }
}
