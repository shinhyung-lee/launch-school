'''
PEDAC
Input:  takes two list arguments, each containing a list of numbers
Output: a new list that contains the product of each pair of numbers from 
        the arguments that have the same index.

Rules:
Explicit:
    -arguments contain the same number of elements 

Questions:
    - can lists be empty? 

Data Structures:

Algorithms:
    - initialize an empty list "multiplied"
    - iterate through both lists using the length of one list
        - declare a variable "multiple" as a multiplication of numbers from list1 and list2 on the same index
        - append "multiple" to "multiplied"
    - return "multiplied"
'''

def multiply_list(lst1, lst2):
    multiplied = []
    for idx in range(len(lst1)):
        multiple = lst1[idx] * lst2[idx]
        multiplied.append(multiple)
    return multiplied

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

list1 = []
list2 = []
print(multiply_list(list1, list2) == [])  # True

# second method using zip
def multiply_list2(lst1, lst2):
    return [num1 * num2 for num1, num2 in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list2(list1, list2) == [27, 50, 77])  # True

list1 = []
list2 = []
print(multiply_list2(list1, list2) == [])  # True