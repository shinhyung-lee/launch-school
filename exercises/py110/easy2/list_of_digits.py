''' 
PEDAC

Input:  A number
Output: A list of the digits in the number from the input number

Data Structures:
    - string: convert number to string
    - list: iterate through string, compose list out of that string

Algorithms:
    - initialize stringified_num as the string converted input "number"
    - initialize an empty string "num_list"
    - Iterate through the string using index, append each number to "num_list"
    - return "num_list"

'''

# method 1
def digit_list(number):
    stringified_number = str(number)
    num_list = []

    for digit in stringified_number:
        num_list.append(int(digit))

    return num_list 

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# method 2
def digit_list2(number):
    return [int(digit) for digit in str(number)]

print(digit_list2(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list2(7) == [7])                       # True
print(digit_list2(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list2(444) == [4, 4, 4])               # True