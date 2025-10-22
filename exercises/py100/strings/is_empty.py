
def is_empty(sentence: str) -> bool:
    return len(sentence) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True