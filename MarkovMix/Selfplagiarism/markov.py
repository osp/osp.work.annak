import random
import re

class Markov(object):
    
    def __init__(self, chunks):
        self.cache = {}
        self.chunks = chunks
        self.words = self.chunks_to_words()
        self.word_size = len(self.words)
        self.out_size = len(self.words)/len(self.chunks)
        self.database()
       
    
    def chunks_to_words(self):
        words = []
        for chunk in self.chunks:
            chunk.text = re.sub(r'<[^>]*?>', '', chunk.text) 
            words.extend(chunk.text.split())
        return words
       
    
    def triples(self):
        """ Generates triples from the given data string. So if our string were
           "What a lovely day", we'd generate (What, a, lovely) and then
           (a, lovely, day).
        """
       
        if len(self.words) < 3:
            return
       
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])
         
    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]
        
    # ${\small \textnormal{\useTextGlyph{fxl}{summation}}}$
    def generate_markov_text(self):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in xrange(self.out_size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)
         
         