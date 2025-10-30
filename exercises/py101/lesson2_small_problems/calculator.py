import json

LANGUAGE = 'en'

with open("config.json", 'r') as file:
    prompts = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True 

    return False 

def invalid_bool(bool_str):
    if bool_str.casefold() in ['y', 'n']:
        return False 
    else:
        return True 

program_continue = True 

prompt('Welcome to Calculator!\n Bienvenido, elige tu idioma\n')
language = input("Choose language. 1) English 2) Espanol: ")

while language not in ["1", "2"]:
    prompt("Invalid number.")
    language = input("Choose language. 1) English 2) Espanol: ")

lang = "en" if language == "1" else "es"

while program_continue:

    prompt(prompts[lang]["first number"])
    number1 = input()
    while invalid_number(number1):
        prompt(prompts[lang]["invalid number"])
        number1 = input()

    prompt(prompts[lang]["second number"])
    number2 = input()

    while invalid_number(number2):
        prompt(prompts[lang]["invalid number"])
        number2 = input()

    operation = input(prompts[lang]["choose operation"])

    match operation:
        case '1':
            output = float(number1) + float(number2) 
        case '2':
            output = float(number1) - float(number2) 
        case '3':
            output = float(number1) * float(number2) 
        case '4':
            output = float(number1) / float(number2) 
    
    while operation not in ["1", "2", "3", "4"]:
        print("incorrect operation chosen. Try again.")
        operation = input(prompts[lang]["choose operation"])

    print(f"The result is: {output}")

    # answer
    program_continue_raw = input(prompts[lang]["continue message"])
    # needs to be Y/N or y/n (use casefold)
    # if not valid bool, prompt user to enter continue value again
    while invalid_bool(program_continue_raw):
        print("incorrect boolean value chosen. Try again.")
        program_continue_raw = input(prompts[lang]["continue message"])

    program_continue = (program_continue_raw.casefold() == 'y')




