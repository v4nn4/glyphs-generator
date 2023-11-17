# glyphs-generator

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