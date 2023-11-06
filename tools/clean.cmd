@echo off
call conda activate glyphs-generator-env
black ..\glyphs_generator
isort ..\glyphs_generator
nbqa black ..
nbqa isort ..
call conda deactivate