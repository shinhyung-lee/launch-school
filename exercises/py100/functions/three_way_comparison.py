def compare_by_length(sentence1, sentence2):
    if len(sentence1) == len(sentence2):
        return 0 
    elif len(sentence1) < len(sentence2):
        return -1
    else:
        return 1
    
def compare_by_length2(str1, str2):
    return (len(str1) > len(str2)) - (len(str1) < len(str2))

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

print(compare_by_length2('patience', 'perseverance')) # -1
print(compare_by_length2('strength', 'dignity'))      #  1
print(compare_by_length2('humor', 'grace'))           #  0