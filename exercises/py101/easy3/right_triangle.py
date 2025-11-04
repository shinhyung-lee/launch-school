

def triangle(height):
    for num_star in range(1, height + 1):
        num_padding = height - num_star 
        print(f"{" " * num_padding}{"*" * num_star}")


triangle(5)
triangle(9)