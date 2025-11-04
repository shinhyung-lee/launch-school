def center_of(sentence):
    if len(sentence) % 2 == 1:
        center_index = len(sentence) // 2
        return sentence[center_index]
    else:
        left_index = len(sentence) // 2 - 1
        return sentence[left_index:left_index + 2]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True