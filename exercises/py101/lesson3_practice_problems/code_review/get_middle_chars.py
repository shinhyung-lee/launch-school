


def center_of(sentence: str):
    if len(sentence) % 2 == 0: # even, return 2 chars "launch"
        left_index = len(sentence) // 2 - 1
        return sentence[left_index:left_index + 2]
    else: # odd, return 1 char "chard"
        middle_index = len(sentence) // 2
        return sentence[middle_index]


# These examples should all print True
print(center_of('I love Python!!!') == "Py")
print(center_of('Launch School') == " ")
print(center_of('Launchschool') == "hs")
print(center_of('Launch') == "un")
print(center_of('Launch School is #1') == "h")
print(center_of('x') == "x")