# glyphs-generator

<p>
<a href="https://github.com/v4nn4/glyphs-generator/actions"><img alt="Actions Status" src="https://github.com/v4nn4/glyphs-generator/actions/workflows/test.yml/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


A glyph generation tool with specified constraints:

- Glyphs are deemed identical if they can be converted into one another through rotation, or by flipping them horizontally or vertically
- With the exception of single-stroke glyphs, each stroke must intersect with another stroke

The tool examines a sequence of potential strokes and computes the equivalence classes for glyphs composed of any stroke combination.

## Alphabet generation

We generated alphabets based on some glyph primitives with 6 strokes or 8 strokes.

### 6-A

![primitives_6-A](assets/glyphs_6a.png)

### 6-B

![primitives_6-B](assets/glyphs_6b.png)

### 6-C

![primitives_6-C](assets/glyphs_6c.png)

### 8-A

![primitives_8-A](assets/glyphs_8a.png)

### 10-A

![primitives_8-A](assets/glyphs_10a.png)