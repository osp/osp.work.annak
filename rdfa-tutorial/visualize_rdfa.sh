#! /usr/bin/env bash

# Creates an visualization of what's in a store
#
# Usage ./visualize_rdfa.sh page.html
# Outputs page.svg

rdfproc -c store parse "${1}" rdfa
rdfproc store serialize dot | dot -Tsvg > $(basename "${1}" .html).svg
rm *.db
