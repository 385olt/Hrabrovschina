from os import listdir
from os.path import isfile, join
import random
import re

DATA_DIR = 'data'
ALLOWED_SYMBOLS_REGEX = '[^\w\,\.\!\?\-]'

data_files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

first_words = list()
last_words = list()
dictionary = dict()

for data_file in data_files:
    f = open(DATA_DIR + "/" + data_file, "r")
    for line in f:
        sentence = line.strip()
        words = [re.sub(ALLOWED_SYMBOLS_REGEX, '', s) for s in sentence.split()]
        first_words.append(words[0])
        last_words.append(words[-1])
        for i in range(1, len(words)):
            if words[i-1] not in dictionary:
                dictionary[words[i-1]] = list()
            dictionary[words[i-1]].append(words[i])


result = random.choice(first_words)
last_word = result
while last_word not in last_words:
    if last_word in dictionary:
        last_word = random.choice(dictionary[last_word])
    else:
        last_word = random.choice(list(dictionary.keys()))

    result += " " + last_word

print(result)
