'''
Input: string
Output: None
        - prints longest string
        - how long the sentence is (# of words)
        
Data Structure:
- list: (store sentences)
- int: # of words in the longest string 
- string: split sentences into strings
'''

def longest_sentence(long_text):
    # ending_chars = '.!?'
    longest_sentence_info = {'sentence': '', 'length': 0}
    
    words = long_text.split()
    curr_sentence = ''
    curr_length = 0 
    for word in words:
        if curr_sentence == '':
            curr_sentence += word
        else:
            curr_sentence += (' ' + word)
            
        curr_length += 1
        if word.endswith(('!', '.', '?')):
            if curr_length > longest_sentence_info['length']:
                longest_sentence_info['sentence'] = curr_sentence 
                longest_sentence_info['length'] = curr_length 
            curr_sentence = ''
            curr_length = 0 
    
    longest_length = longest_sentence_info['length']
    print(longest_sentence_info['sentence'])
    print()
    print(f'The longest sentence has {longest_length} words.')
    print()
        

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)


# Test 1
longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

# Test 2
longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

# Test 3
longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

# Test 4
longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.