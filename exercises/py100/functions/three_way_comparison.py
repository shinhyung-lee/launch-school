



def compare_by_length(sentence1, sentence2):
    if len(sentence1) == len(sentence2):
        return 0 
    elif len(sentence1) < len(sentence2):
        return -1
    else:
        return 1

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0