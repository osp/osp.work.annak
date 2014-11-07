# Markmix: train markov generator with fragments of Kavan and Kafka
# see what comes out

import markov

ak = open("NewAndSplendid.txt", "r")
fk = open("TheStoker.txt", "r")
o = open("markovmix-kafan.txt", "w")

class Chunk():
    def __init__(self, txtfile):
        self.text = txtfile.read()

c1 = Chunk(ak)
c2 = Chunk(fk)
chunks = [c1, c2]

markmixer = markov.Markov(chunks)

out = markmixer.generate_markov_text()

o.write(out)
o.close()
