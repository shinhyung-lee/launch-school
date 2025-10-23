

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = [ int(value / 2) for value in numbers.values() ]
print(half_numbers)