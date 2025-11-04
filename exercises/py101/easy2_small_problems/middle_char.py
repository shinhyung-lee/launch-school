def center_of_even_sentence(sentence):
    # launch len(sentence) // 2 = 3 - 1
    left_index = len(sentence) // 2 - 1
    return sentence[left_index:left_index + 2]

def center_of_odd_sentence(sentence):
    # odd len(sentence) // 2 = 1
    center_index = len(sentence) // 2 
    return sentence[center_index]

def center_of(sentence):
    # assume len(sentence) > 0 
    if len(sentence) % 2 == 1:
        return center_of_odd_sentence(sentence)
    else:
        return center_of_even_sentence(sentence)

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True