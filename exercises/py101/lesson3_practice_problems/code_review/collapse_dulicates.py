

def crunch(sentence):
    if len(sentence) < 2:
        return sentence
    target_char = ""
    result = ""
    for _, current_char in enumerate(sentence):
        if current_char == target_char:
            continue
        else:
            result += current_char
            target_char = current_char

    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

def crunch2(sentence):
    index = 0 
    result = ""
    
    while index < len(sentence):
        if index == len(sentence) - 1 or (sentence[index] != sentence[index + 1]):
            result += sentence[index]
        index += 1
        
    return result    


print(crunch2('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch2('4444abcabccba') == '4abcabcba')
print(crunch2('ggggggggggggggg') == 'g')
print(crunch2('abc') == 'abc')
print(crunch2('a') == 'a')
print(crunch2('') == '')