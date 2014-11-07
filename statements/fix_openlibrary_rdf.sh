#! /usr/bin/env bash

sed -i 's/\(http:\/\/openlibrary.org\/\(authors\|works\|books\)\/[0-9A-Z]\+\)\(\/\)\?"/\1"/g' openlibrary/*.rdf
