import random
import pickle

DICTIONARY_FILE = 'dictionary.pickled'

dictionary_jar = pickle.load(open(DICTIONARY_FILE, 'rb'))

first_words = dictionary_jar['first_words']
last_words  = dictionary_jar['last_words']
dictionary  = dictionary_jar['dictionary']

result = random.choice(first_words)
last_word = result
while last_word not in last_words:
    if last_word in dictionary:
        last_word = random.choice(dictionary[last_word])
    else:
        last_word = random.choice(list(dictionary.keys()))

    result += " " + last_word

print(result)
