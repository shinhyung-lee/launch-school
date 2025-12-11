'''
Input:  A string
Output: A dictionary containing percentage of 1) lowercase letters
2) uppercase letters 3) characters that are neither

Rules
Explicit:
- All three percentages should be returned as string whose numeric 
values lie between "0.00" and "100.00" 
- Each value should be rounded to two decimal points.
- String always contain at least one character

Data Structure:
- Dictionary : containing percentages
- Float      : two decimal points
- String     : f-string

Algorithms:
IDEA
- define a dictionary TALLY with three keys: lower, upper, neither.
Values should be all 0.
- for each character in the input string, check whether it's lower, 
upper, or neither. Tally total to TALLY dictionary
- Out of the values for lower, upper, and neither compute a return
dictionary with three keys lower, upper, and neither

Pseudocode:
- TALLY = { lower: 0, upper: 0, neither: 0 }
- for char in string:
    - tally occurrence to proper key values
- declare return_dict and set values to percentages of each key
    (round to two decimal digits)
- return return_dict
'''

def letter_percentages(string):
    tally = { 'lower': 0, 'upper': 0, 'neither': 0 }
    for char in string:
        if char.islower():
            tally['lower'] += 1
        elif char.isupper():
            tally['upper'] += 1
        else:
            tally['neither'] += 1
    num_lower = tally['lower']
    num_upper = tally['upper']
    num_neither = tally['neither']
    sum_total = sum([num_lower, num_upper, num_neither])
    return {
        'lowercase': f'{num_lower / sum_total * 100:.2f}',
        'uppercase': f'{num_upper / sum_total * 100:.2f}',
        'neither':   f'{num_neither / sum_total * 100:.2f}'
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)