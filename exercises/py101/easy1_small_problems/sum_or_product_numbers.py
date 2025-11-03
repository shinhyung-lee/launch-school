
# PEDAC

# edge case: if integer is less than or equal to 0 
# if integer not in the right range, or the type of data isn't correct, ask user to input again 
# s or p: sum or product
# if user input is not "s" or "p", ask user to input again 
# data structure: range

def get_number():
    while True:
        str_number = input("Please enter an integer greater than 0: ")
        try:
            number = int(str_number)
            if number > 0:
                return number 
            else:
                print("Number must be greater than 0")
        except ValueError:
            print("Please enter an integer greater than 0.")
            
def get_operator():
    while True:
        operator = input("Enter \"s\" to compute the sum, or \"p\" to compute the product. ")
        if operator not in ["s", "p"]:
            print("Please enter \"s\" to compute the sum, or \"p\" to compute the product. ")
        else:
            return operator 

def sum_numbers(number):
    return sum(range(1, number + 1))

def multiply_numbers(number):
    result = 1
    for num in range(1, number + 1):
        result *= num 
    return result 

number = get_number()
operator = get_operator()

match operator:
    case "s":
        print(f"The sum of the integers between 1 and {number} is {sum_numbers(number)}")
    case "p":
        print(f"The product of the integers between 1 and {number} is {multiply_numbers(number)}")
    
        

