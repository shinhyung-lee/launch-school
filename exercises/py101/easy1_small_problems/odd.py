# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

def is_abs_odd(num: int) -> bool:
    # python function for absolute value? 
    # abs_num = abs(num)
    # Using modulo operation, Return True if the number has a modulo 0 when divided by 2. Otherwise, return False.
    abs_num = abs(num)
    is_odd = abs_num % 2 == 1
    return is_odd 

if __name__ == "__main__":
    assert is_abs_odd(3) == True 
    assert is_abs_odd(-6) == False 
    print(is_abs_odd(100))
    print(is_abs_odd(-99))
    
    