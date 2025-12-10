'''
Input:  a string
Output: a string from the input, but every occurrence of a "number word" converted to its corresponding digit character

Rules
Explicit:
    - string does not contain any punctuation

Data Structures:
    - dictionary to match "number word" to "digit character".

Algorithms:
    - DIGITS = { "zero": '0', "one": '1', etc... }
    - results = []
    - for word in string.split():
        - if word is in digit, replace the word with its corresponding value and add to results
        - otherwise, add to results as is
    - return " ".join(results)
'''


def word_to_digit(string):
    DIGITS = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    results = []
    for word in string.split():
        if word in DIGITS:
            results.append(DIGITS[word])
        else:
            results.append(word)
    
    return " ".join(results)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True