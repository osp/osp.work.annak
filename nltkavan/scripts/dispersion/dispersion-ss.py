#! /usr/bin/env python2

import nltk

file = open("../osp.work.annak.books/AK/AStrangerStill/a_stranger_still.txt", "r")
raw = file.read()
file.close()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

ss_locations = ["Starling Hill","Worcester Road","Ethelbert Place","London","Thazila","Nice","Bandol", "Toulon", "Riviera","Gardone"]
ss_names = ["William","Cedric","Jean","Martin","Germaine","Gwenda","Gerald","Anthony","Tony", "Hubert","David","George","Winny","Edward","Anna","Matthew","Catherine","Mary", "Claydon","I","you", "he", "she", "we", "they"]

# text.dispersion_plot(ss_locations)
text.dispersion_plot(ss_names)
