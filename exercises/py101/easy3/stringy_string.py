

def stringy(num):
    result_string = ""
    for idx in range(num):
        digit = '1' if idx % 2 == 0 else '0'
        result_string += digit
    return result_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True