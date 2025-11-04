

def crunch(sentence):
    result = ''
    # iterate using index, if s[curr] != s[curr + 1], add to string
    for idx, _ in enumerate(sentence):
        if idx == len(sentence) - 1 or sentence[idx] != sentence[idx + 1]:
            result += sentence[idx]
    return result
        
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')