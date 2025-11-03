

# returns short long short
def short_long_short(sentence1, sentence2):
    # assume the strings are of different lengths
    long = sentence1 if len(sentence1) > len(sentence2) else sentence2
    short = sentence2 if len(sentence1) > len(sentence2) else sentence1 
    return f"{short}{long}{short}"

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
    