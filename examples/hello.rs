extern crate glyphs_generator;
use glyphs_generator::run;
use std::fs;

fn main() {
    let file_content = fs::read_to_string(
        "/Users/romflorentz/Documents/Repos/glyphs-generator/examples/input.json",
    )
    .expect("Failed to read file")
    .to_string();
    let output = run(file_content);
    println!("{}", output);
}
