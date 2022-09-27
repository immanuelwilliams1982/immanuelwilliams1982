//PIP INSTALL THE IMPORTED PACKAGES BEFORE WRITING AND EXECUTING THIS CODE
from random_word import RandomWords
from PyDictionary import PyDictionary


r = RandomWords()
dct=PyDictionary()

w=r.get_random_word()
print(w)

print (dct.meaning(w))
