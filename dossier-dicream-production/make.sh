#! /usr/bin/env zsh

pandoc -f markdown -t context -o bilan-v2-1.tex bilan-v2-1.md
context template.tex
