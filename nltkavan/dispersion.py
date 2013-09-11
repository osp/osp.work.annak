import nltk

#file = open("../books-AK/Ice/Ice.txt", "r")
file = open("../plagiat/vonnegut/Cat's_Cradle.txt", "r")
raw = file.read()
file.close()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

ice_locations = ["Atlantic", "Britain", "Cologne", "France", "United", "States"]
ice_names = ["Anna", "Dennis", "Dick", "Helen", "John", "Jorge", "K.", "Luis", "M.", "Owen", "Paul", "Peter", "Philip", "Potter", "S.", "Stone", "Thomas", "William"]

cat_locations = ["China", "Cuba", "England", "Florida", "France", "Germany", "Hollywood", "Hong", "Kong", "India", "Indianapolis", "Japan", "London", "Manhattan", "Newport", "Newton", "N.Y.", "New", "York", "Puerto", "Rhode", "Russia", "San", "Lorenzo", "Santa", "Tokyo"]

cat_names = ["Albert", "Schweitzer", "Barbara", "Hutton", "Betsy", "Ross", "Lionel", "Boyd", "Harrison", "C.", "Conners", "Castle", "Cedar", "Charles", "Atlas", "David", "McCabe", "Felix", "Frank", "Franklin", "H.", "Lowe", "Crosby", "Harry", "Truman", "I", "Jack", "Johnson","Julian", "Castle", "Lewis", "Marvin", "Breed", "Faust", "Pefko", "Fata", "Morgana", "Newton", "Hoenikker", "Philip", "Robinson", "Sandra", "Stanley"]


text.dispersion_plot(cat_locations)
