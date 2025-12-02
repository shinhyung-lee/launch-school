'''
converts a string representing a hexadecimal number to its integer value.
Hexadecimal numbers use base 16 instead of 10, and the characters A, B, C, D, E and F 
(and the lowercase equivalents) correspond to decimal values of 10-15.

'''

def hexadecimal_to_integer(hex_string):
    HEX_DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    
    value = 0 
    for char in hex_string:
        hex_value = char.upper() if char.isalpha() else char 
        value = (16 * value) + HEX_DIGITS[hex_value]
    return value


print(hexadecimal_to_integer('4D9f') == 19871)  # True
print(hexadecimal_to_integer('0') == 0)
print(hexadecimal_to_integer('aa') == 170)
print(hexadecimal_to_integer('Fa6e8') == 1025768)
