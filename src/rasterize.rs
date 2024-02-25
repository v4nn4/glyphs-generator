use crate::Coordinate;
use crate::Stroke;

pub fn world_to_view(coordinate: &Coordinate) -> (usize, usize) {
    let dimension = 9;
    let half = (dimension as f64 - 1.0) / 2.0;
    (
        ((coordinate.x * half + half).round() as usize).min(dimension - 1),
        ((coordinate.y * half + half).round() as usize).min(dimension - 1),
    )
}

pub fn rasterize(strokes: &Vec<Stroke>, dimension: usize) -> Vec<Vec<u8>> {
    let mut array = vec![vec![0u8; dimension]; dimension];

    for stroke in strokes {
        rasterize_stroke(stroke, dimension, &mut array);
    }
    array
}

pub fn rasterize_stroke(stroke: &Stroke, dimension: usize, array: &mut Vec<Vec<u8>>) {
    let (x0, y0) = world_to_view(&stroke.start);
    let (x1, y1) = world_to_view(&stroke.end);
    array[y0][x0] = 1;
    array[y1][x1] = 1;

    if x0 == x1 {
        for y in std::cmp::min(y0, y1)..=std::cmp::min(std::cmp::max(y0, y1), dimension - 1) {
            array[y][x0] = 1;
        }
    } else if y0 == y1 {
        for x in std::cmp::min(x0, x1)..=std::cmp::min(std::cmp::max(x0, x1), dimension - 1) {
            array[y0][x] = 1;
        }
    } else {
        let slope = (x1 as f64 - x0 as f64) / (y1 as f64 - y0 as f64);
        for y in std::cmp::min(y0, y1)..=std::cmp::min(std::cmp::max(y0, y1), dimension - 1) {
            let x =
                ((slope * (y as f64 - y0 as f64) + x0 as f64).floor() as usize).min(dimension - 1);
            array[y][x] = 1;
        }
    }
}
