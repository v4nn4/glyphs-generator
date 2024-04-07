use std::collections::HashSet;

use crate::stroke::InternalStroke;
use crate::stroke::Stroke;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Glyph {
    pub strokes: Vec<Stroke>,
}

impl PartialEq for Glyph {
    fn eq(&self, other: &Self) -> bool {
        let self_set: HashSet<_> = self.strokes.iter().collect();
        let other_set: HashSet<_> = other.strokes.iter().collect();

        self_set == other_set
    }
}

impl Eq for Glyph {}

#[derive(Debug, Clone)]
pub struct InternalGlyph {
    pub strokes: Vec<InternalStroke>,
    pub identifier: u64,
}

impl InternalGlyph {
    pub fn empty() -> Self {
        InternalGlyph {
            strokes: vec![],
            identifier: 0,
        }
    }

    pub fn from_stroke(stroke: InternalStroke) -> Self {
        let identifier = 1 << stroke.index;
        InternalGlyph {
            strokes: vec![stroke],
            identifier,
        }
    }

    pub fn union(&self, other: &Self) -> Self {
        let mut indices: Vec<usize> = self.strokes.iter().map(|s| s.index).collect();
        indices.extend(other.strokes.iter().map(|s| s.index));

        let unique_indices: Vec<usize> = indices
            .into_iter()
            .collect::<std::collections::HashSet<_>>()
            .into_iter()
            .collect();
        let new_strokes: Vec<InternalStroke> = unique_indices
            .into_iter()
            .map(|index| InternalStroke { index })
            .collect();

        InternalGlyph {
            strokes: new_strokes,
            identifier: self.identifier | other.identifier,
        }
    }
}

impl PartialEq for InternalGlyph {
    fn eq(&self, other: &Self) -> bool {
        self.identifier == other.identifier
    }
}

impl Eq for InternalGlyph {}
