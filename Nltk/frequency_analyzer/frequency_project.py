from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

data = open("data.txt", 'r')
print(data.read())
data.close()