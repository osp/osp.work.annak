#! /usr/bin/env bash

# Outputs a list of words in the text and the number of times they appear
# Ordered from the most frequent word to the least one.
#
# USAGE
#
# ./index.sh /path/to/file.txt


cat $1 | tr -d "[:punct:]"  | tr " " "\n" | sort  | uniq -ci | sort -nr
