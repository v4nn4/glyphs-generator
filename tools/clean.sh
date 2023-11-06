#!/bin/bash
source /users/romflorentz/miniconda3/bin/activate glyphs-generator-env
black "../glyphs_generator"
isort "../glyphs_generator"
nbqa black ..
nbqa isort ..
conda deactivate