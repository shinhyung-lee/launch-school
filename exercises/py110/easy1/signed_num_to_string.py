

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def integer_to_string(integer):
    stringified_num = ""

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        stringified_num = DIGITS[remainder] + stringified_num
    
    return stringified_num or "0"

def signed_integer_to_string(number):
    if number == 0:
        return "0"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return f"-{integer_to_string(-number)}"



print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True