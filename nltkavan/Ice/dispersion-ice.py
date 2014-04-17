import nltk

file = open("../osp.work.annak.books/AK/Ice/Ice.txt", "r")
raw = file.read()
file.close()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

ice_locations = ["ice", "town", "country","north","region","High", "House"]
ice_names = ["girl", "husband", "warden","I", "you", "he", "she", "we", "they"]

# text.dispersion_plot(ice_locations)
text.dispersion_plot(ice_names)


       
 
      
       

 
     
