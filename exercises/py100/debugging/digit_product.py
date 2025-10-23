

# whatever we multiply to 0, result will be 0
# we have to initialize product's innitial value to 1

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0