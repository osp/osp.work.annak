import nltk

file = open("../osp.work.annak.books/AK/LetMeAlone/let_me_alone-all.txt", "r")
raw = file.read()
file.close()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

lma_locations = ["Blue Hills","River House", "Port Said", "Oxford", "London","Rangoon"]
lma_names = ["Wilson","Heyward","Lauretta","James","Rachel","Catherine","Sidney","Anna","Forrester","Matthew", "Kavan","I","you","he","she","we","they"]

# text.dispersion_plot(lma_locations)
text.dispersion_plot(lma_names)
