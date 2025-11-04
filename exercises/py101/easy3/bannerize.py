

def print_in_box(text):
    horizontal_rule = f'+-{'-' * len(text)}-+'
    empty_rule = f'| {' ' * len(text)} |'

    print(horizontal_rule)
    print(empty_rule)
    print(f'| {text} |')
    print(empty_rule)
    print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')