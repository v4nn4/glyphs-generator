![alt text](./assets/glyphs_hero.png)

# glyphs-generator | [demo](https://v4nn4.github.io/glyphs-generator/)

<p>
<a href="https://github.com/v4nn4/glyphs-generator/actions"><img alt="Actions Status" src="https://github.com/v4nn4/glyphs-generator/actions/workflows/test.yml/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A glyph generation tool with geometric constraints.

👉 Companion blog post: https://v4nn4.github.io/posts/glyph-generation/.

## Concept

The idea is to generate glyphs from a set of points on a grid. Since the number of possible glyphs increases exponentially with the number of points, we apply some geometrical constraints to narrow down our search. We then derive an efficient search algorithm.

## Playground

A playground is available [here](https://v4nn4.github.io/glyphs-generator/) for you to try! It is based on a blazing fast [Rust implementation](https://github.com/v4nn4/glyphs-generator-rs) that runs in the browser using WebAssembly and wasm-bindgen.
