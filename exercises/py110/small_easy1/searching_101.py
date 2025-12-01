
def number_included(numbers, target):
    return target in numbers

num1 = input('Enter the 1st number: ')
num2 = input('Enter the 2nd number: ')
num3 = input('Enter the 3rd number: ')
num4 = input('Enter the 4th number: ')
num5 = input('Enter the 5th number: ')
target_num = input('Enter the 6th number: ')

numbers = []
numbers.extend([num1, num2, num3, num4, num5])

included = number_included(numbers, target_num)
print(f"{target_num} {'is' if included else "isn't"} in {",".join(numbers)}.")

