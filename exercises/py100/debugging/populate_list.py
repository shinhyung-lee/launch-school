
# range function starts from number 0. also if we say range(5), it's a range of numbers from
# 0 to 4 inclusive. Therefore, we fix the range part to range(1, 6)

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)