


def sequence(target):
    nums = []
    for num in range(1, target + 1):
        nums.append(num)
    return nums

print("Method 1")
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

def sequence2(target):
    return list(range(1, target + 1))

print("\nMethod 2")
print(sequence2(5) == [1, 2, 3, 4, 5])   # True
print(sequence2(3) == [1, 2, 3])         # True
print(sequence2(1) == [1])               # True