#! /usr/bin/env bash

# USAGE
#
# Outputs a 3 column list of words: 1 = words only in file1; 2 = words only in file2; 3 = words in both texts
# ./compare.sh /path/to/file1.txt /path/to/file2.txt
#
# Outputs a list of common words of two texts
# ./compare.sh /path/to/file1.txt /path/to/file2.txt common

if [ "$3" = "common" ];
    then
        comm -12 $1 $2
    else
        comm $1 $2
fi
