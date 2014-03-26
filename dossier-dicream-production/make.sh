#! /usr/bin/env zsh

pandoc -f markdown -t context -o bilan-v2-1.tex --chapters bilan-v2-1.md
sed -i 's/here,nonumber/force,nonumber/g' bilan-v2-1.tex
context template.tex
