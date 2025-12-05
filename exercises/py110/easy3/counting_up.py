


def sequence(target):
    nums = []
    for num in range(1, target + 1):
        nums.append(num)
    return nums

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True