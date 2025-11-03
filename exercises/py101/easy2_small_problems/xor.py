
# Return True only if one of the arguments are Truthy, False otherwise
# False, True (or, and)  (arg1 and arg2 == False) and (arg1 or arg2 == True)
# True False
def xor(arg1, arg2):
    if (arg1 and not arg2) or (not arg1 and arg2):
        return True
    
    return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)