import os
import re

filename = "quiz.html"

content = ""

# Open the file in read mode
with open(filename, 'r') as f:
    # Read the content of the file
    content = f.read()

# dictionary to store the questions and answers
questions = {}

# parse the content.
# scrap questions and answers
# and store them in the dictionary
# search for "Flashcard\",\"text\":\"• Tyčinky\", extract Tyčinky as question
# "Answer\",\"text\":\"neslouží k ostrému vidění\", extract neslouží k ostrému vidění as answer
# etc.


# OTHER PATTERN
# "word\":\"• Co není denzitometrie\",\"_wordTtsUrl\":null,\"_wordSlowTtsUrl\":null,\"_wordAudioUrl\":null,\"definition\":\"něco se zubama\",

words = re.findall(r'"word\\":\\"([^\\]*)\\', content)
definitions = re.findall(r'"definition\\":\\"([^\\]*)\\', content)
# strip "• " from the beginning of the word if present
words = [re.sub(r'^• ', '', word) for word in words]

# create a dictionary of words and definitions
questions = dict(zip(words, definitions))

# print the dictionary
for key, value in questions.items():
    print(key, " : ", value)


