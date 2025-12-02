'''
PEDAC
Write a function that takes a string consisting of zero or more space-separated words and returns 
a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

Input  : string consisting of zero or more space-separated words
Output : a dictionary that shows the number of words of different sizes

Rules
Explicit: 
    -words are separated by space
    -there can be zero or more words
Implicit:
    -If the input string is empty, returning dictionary will be an empty dict

Questions:
    -We consider non-alphanumeric characters when counting the length of a word

Data Structure:
    - list: convert input string into a list of words delimited with spaces.
    - dictionary: to keep track of the number of words of different sizes

Algorithm:
    - Initialize a result dictionary "word_frequency_dict" as an empty dictionary
    - Initialize a list / array containing the words from the string delimited by a space as 
    "words"
    - Iterate through the words in "words".
        -Count the length of word and store the value in a variable "word_length"
        -increment the value from dictionary that has word_length as a key value
    - return "word_frequency_dict"
'''

# All of these examples should print True
def word_sizes(string):
    if string == '': # guard clause
        return {}
    
    word_frequency_dict = {}
    words = string.split(" ")

    for word in words:
        word_length = len(word)
        word_frequency_dict.setdefault(word_length, 0)
        word_frequency_dict[word_length] += 1 
    
    return word_frequency_dict

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})