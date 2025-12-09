'''
Input:  A string
Output: A list that contains every word from the string, with each word followed by a space and the word's length 

Rules
Explicit:
    - if the argument is an empty string or no argument is passed, function returns an empty list 
    - Every pair of words in the string will be separated by a SINGLE SPACE

Data Structures
    - list : 
    - string : f-string for string interpolation
Algo:
IDEA:
    - Separate every word from the input string, form a list "WORDS".
        - Delimiter will be a single space
    - WORDS_WITH_LENGTHS = []
    - For every word, form a string "{word} {len(word)}"
        - append the f-string to WORDS_WITH_LENGTHS
    - return WORDS_WITH_LENGTHS
'cow cat'
WORDS = ['cow', 'cat']
WORDS_WITH_LENGTHS = ['cow 3', 'cat 3']
return WORDS_WITH_LENGTHS

Pseudocode:
    - words = string.split(' ')
    - words_with_lengths = []
    - for word in words:
        words.append(f'{word} {len(word)}')
    - return words
'''

def word_lengths(string = ''):
    if len(string) == 0:
        return []
    
    words = string.split(' ')
    words_with_lengths = []
    for word in words:
        words_with_lengths.append(f'{word} {len(word)}')
    return words_with_lengths

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True