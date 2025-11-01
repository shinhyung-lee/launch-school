# 

def compute_sum(target_number: int):
    return sum(range(1, target_number + 1))

def compute_multiply(target_number: int):
    product = 1 
    for num in range(1, target_number + 1):
        product *= num 
    return product


def compute(target_num: int, operator: str):
    match operator:
        case "+":
            return compute_sum(target_num)
        case "*":
            return compute_multiply(target_num)
        case _:
            return None

# These examples should all print True
print(compute(5, '+') == 15)
print(compute(6, '*') == 720)
print(compute(7, '-') == None)
