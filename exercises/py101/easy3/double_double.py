def is_double_double(num):
    str_num = str(num)
    center = len(str_num) // 2
    left_number = str_num[:center]
    right_number = str_num[center:]

    return left_number == right_number

def twice(num):
    if is_double_double(num):
        return num
    else:
        return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True