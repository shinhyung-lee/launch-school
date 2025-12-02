'''
Prompt: 
Given a string of words separated by spaces, 
write a function that swaps the first and last letters of every word.

Input:  A string of words separated by spaces
Output: A string but in every word in the input string, the first and last letters are swapped.

Rules
Explicit:
    - Assume that every word contains at least one letter
    - string will always contain at least one word
    - each string contains nothing but words and spaces, and that there are no leading, 
      trailing, or repeated spaces.
Implicit:

Questions:

Data Structure:
    - string: to store the result string
    - list: 1) store all words from the original string 2) swap first and last letters from original words
            and store them in this new list 

Algorithm:
    - Declare a "result" string that will hold the final result
    - Store words from the original string into a list "words", delimited by spaces
    - Initialize an empty list "new_words"
    - Iterate each word in "words" list
        -swap first and last letters
            -append this swapped word to new_words 
    - Join new_words list into a string "result"
    - Return "result"

Helper Function def swap_letters(word)

Input:  a word
Output: a word from input, but first and last letters are swapped

Rules:
Explicit:

Implicit:

'''

def swap_letters(word):
    if len(word) == 1:
        return word 
    
    return word[-1] + word[1:-1] + word[0]

def swap(string):
    words = string.split()
    for idx, word in enumerate(words):
        words[idx] = swap_letters(word)
    return ' '.join(words)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True