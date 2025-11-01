
# left side digits are the same as the right side digits 
# if not a double number, return original number * 2

def is_double_number(number):
    # assume even length number 
    string_number = str(number)
    center_index = len(string_number) // 2
    left_number = string_number[:center_index]
    right_number = string_number[center_index:]

    return left_number == right_number


def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2

# These examples should all print True
print(twice(37) == 74)
print(twice(44) == 44)
print(twice(334433) == 668866)
print(twice(444) == 888)
print(twice(107) == 214)
print(twice(103103) == 103103)
print(twice(3333) == 3333)
print(twice(7676) == 7676)