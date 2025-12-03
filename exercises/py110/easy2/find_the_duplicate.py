'''

Input: an unordered list of numbers in which exactly one value in the list occurs twice
Output: a value from the input list that occurs twice  

Rules
Explicit:
    - Exactly one value is a duplicate in the list
Implicit:

Questions:
    - can the list have strings or other types?

Data Structures:
    - dictionary 

Algorithms:
    - initialize a dictionary named "counter" and assign empty dictionary to it
    - iterate through the list "nums" provided as an argument to the function,
        - keep track of the counter in "counter" dict
        - "counter".setdefault(value, 0)
        - increment the value by 1
    - iterate through "counter" using dict.items()
        -if the value is 2, return the corresponding key 
'''

def find_dup(nums):
    counter = {}
    for num in nums:
        counter.setdefault(num, 0)
        counter[num] += 1
    for num, frequency in counter.items():
        if frequency == 2:
            return num 

print('Testing first version of find_dup')
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
print(find_dup(['b', 'a', 'c', 'z', 'd', 'a']) == 'a')

def find_dup2(values):
    dup = [value for value in values if values.count(value) == 2]
    return dup[0]

print('Testing second version of find_dup')
print(find_dup2([1, 5, 3, 1]) == 1) # True
print(find_dup2([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
print(find_dup2(['b', 'a', 'c', 'z', 'd', 'a']) == 'a')

def find_dup3(values):
    # using set 
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

print('Testing third version of find_dup')
print(find_dup3([1, 5, 3, 1]) == 1) # True
print(find_dup3([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
print(find_dup3(['b', 'a', 'c', 'z', 'd', 'a']) == 'a')