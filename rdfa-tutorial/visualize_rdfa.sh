#! /usr/bin/env bash

# Creates an visualization of what's in a store
#
# Usage ./visualize_rdfa.sh page.html
# Outputs page.svg

rm *.db
rdfproc -c store parse "${1}" rdfa
rdfproc store serialize dot | circo -Tsvg > $(basename "${1}" .html).svg
