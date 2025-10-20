import random
random_number = random.randint(0, 1)

# use ternary expression
message = 'Yes!' if random_number else 'No.'
print(message)