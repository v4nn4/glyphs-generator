extern crate glyphs_generator;
use glyphs_generator::run;
use std::fs;

fn main() {
    let input = fs::read_to_string(
        "/Users/romflorentz/Documents/Repos/glyphs-generator/examples/input.json",
    )
    .expect("Failed to read input file")
    .to_string();
    let result = run(input);
    println!("{}", result);
}
