

def starts_with(s: str, prefix: str) -> bool: 
    return s.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True