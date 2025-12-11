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
def get_formatted_percentage(num, total):
    return f'{num / total * 100:.2f}'

def letter_percentages(string):
    total_chars = len(string)
    lower = 0
    upper = 0
    neither = 0
    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        else:
            neither += 1

    return {
        'lowercase': get_formatted_percentage(lower, total_chars),
        'uppercase': get_formatted_percentage(upper, total_chars),
        'neither': get_formatted_percentage(neither, total_chars)
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