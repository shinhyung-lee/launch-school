'''
Input  : 
Output : 

Rules
Explicit
    - all arguments are valid programs 
Implicit

Data Structures:
    - list : list.pop(), list.append()
    - match-case 
    - register: INT
    - stack: LIST 
    - parse each argument

Algorithms:
IDEA
    -
Pseudocode:
    - divide each operation into its own function 
'''
def place_number_in_register(num): # might not need this function at all 
    # do not modify the stack, place the int number in the register
    return num 

def push(stack, register):
    stack.append(register) 

def add(stack, register):
    return register + stack.pop() # store this in register 

def sub(stack, register):
    return register - stack.pop() # store this in register 

def mult(stack, register):
    return register * stack.pop() # store this in register 

def div(stack, register):
    return register // stack.pop() # store this in register 

def remainder(stack, register):
    _, remainder = divmod(register, stack.pop())
    return remainder # store this in register 

def miniature_pop(stack):
    return stack.pop() # store this in register 

def print_register(register):
    print(register)

def minilang(prompt):
    operands = prompt.split() # store individual operands into a list 
    stack = []
    register = 0
    while operands: 
        # pop the first element (0-th index)
        operand = operands.pop(0)
        match operand:
            case s if s.lstrip('-').isdigit():
                register = int(operand)
            case 'PUSH':
                push(stack, register)
            case 'ADD':
                register = add(stack, register)
            case 'SUB':
                register = sub(stack, register)
            case 'MULT':
                register = mult(stack, register)
            case 'DIV':
                register = div(stack, register)
            case 'REMAINDER':
                register = remainder(stack, register)
            case 'POP':
                register = miniature_pop(stack)
            case 'PRINT':
                print_register(register)
            


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# # 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# (nothing is printed)