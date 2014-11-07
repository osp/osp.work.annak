# Markmix: train markov generator with fragments of Ice and Mercury
# see what comes out

import markov

i = open("ice-txtonly.txt", "r")
m = open("mercury-txtonly.txt", "r")
o = open("markovmix-kavan.txt", "w")

class Chunk():
    def __init__(self, txtfile):
        self.text = txtfile.read()

c1 = Chunk(i)
c2 = Chunk(m)
chunks = [c1, c2]

markmixer = markov.Markov(chunks)

out = markmixer.generate_markov_text()

o.write(out)
o.close()
