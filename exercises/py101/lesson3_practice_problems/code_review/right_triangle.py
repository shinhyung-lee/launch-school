

def triangle(number):
    # print in each line
    for num_padding in range(1, number + 1):
        line = f"{'*' * num_padding}".rjust(number)
        print(line)

triangle(5)
triangle(9)