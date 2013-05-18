#! /usr/bin/bash

# Outputs a list of all words in a text.
#
# USAGE
#
# ./lexique.sh /path/to/file.txt

cat $1 | tr -d "[:punct:]"  | tr " " "\n" | sort  | uniq -i 

