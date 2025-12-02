'''
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. 
For instance, the word size of "it's" is 3, not 4.

PEDAC
Input  : a string
Output : a dictionary that shows the number of words of different sizes

Rules:
Explicit:
    - Non-letters do not count towards the length of a word
    - 
Implicit:
    - Empty string input will return an empty dictionary output
Questions:


Data Structures
    - list: to store each word
    - dict: to store the result dictionary 

Algorithm: 
    - Initialize a result dictionary "word_frequency_dict" as an empty dictionary
    - Initialize a list / array containing the words from the string delimited by a space as 
    "words"
        -Do not count non-alphabetic characters 
        -Have a helper function that does this

                
def count_word_length(word):
Input  : a word 
Output : length of the word

Rules:
Explicit:
    -exclude non-alphabetic characters
Implicit:

'''

# helper function
def count_word_length(word):
    total = 0

    for char in word:
        if char.isalpha():
            total += 1
    return total

def word_sizes(string):
    if string == '':
        return {}
    words = string.split()
    word_frequency_dict = {}

    for word in words:
        word_length = count_word_length(word)
        if word_length not in word_frequency_dict:
            word_frequency_dict[word_length] = 0
        word_frequency_dict[word_length] += 1
 
    return word_frequency_dict


# All of these examples should print True
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})