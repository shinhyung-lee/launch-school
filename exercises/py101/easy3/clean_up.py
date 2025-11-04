
def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        # if alphabetic, must add to result string
        if char.isalpha():
            clean_text += char
        # if not alphabetic, consider possibilities
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text


print(clean_up("---what's my +*& line?") == " what s my line ")
# True