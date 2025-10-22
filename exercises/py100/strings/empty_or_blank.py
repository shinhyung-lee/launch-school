
def is_empty_or_blank(sentence: str) -> bool: 
    return sentence.isspace() or len(sentence) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True