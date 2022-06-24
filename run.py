""" Pig Latin Translator:
Simple program created to take user input
and translate it to Pig Latin.

Built to sharpen use of input, slice, indexing
if/else statements, conditionals
"""
# create a variable to hold the prefix for each word
PIG = "ay"

# create a variable requesting input from the user
original = input("Ente a word: ")

# check to ensure the the input is longer than 0 characters and is alphabetical
if len(original) >= 0 and original.isalpha():

    print(original)                 # print the original input
    word = original.lower()         # convert it to lowercase characters
    # create variable to hold the first char of the input
    first = word[0]
    # create a new word adding the word, first letter and prefix together
    new_word = word + first + PIG

    new_word = new_word[1:len(new_word)]

# print out a message to let the user know they've entered an usuable string
else:
    print("Empty string")

print(new_word)
