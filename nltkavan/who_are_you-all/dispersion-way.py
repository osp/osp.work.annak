import nltk

file = open("../osp.work.annak.books/AK/WhoAreYou/who_are_you-all.txt", "r")
raw = file.read()
file.close()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

way_locations = ["jungle", "house", "room", "bed"]
way_names = ["girl","birds", "Dog", "Head","rats","Dirwaza","Khan","Suede","Boots","doctor","I", "you", "he", "she", "we", "they"]

# text.dispersion_plot(way_locations)
text.dispersion_plot(way_names)

       
  
       

 
     
