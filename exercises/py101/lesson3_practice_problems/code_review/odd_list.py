

def oddities(collection):
    return [item for (index, item) in enumerate(collection) if index % 2 == 0]

# These examples should all print True
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4]) == [1, 3])
print(oddities(["abc", "def"]) == ['abc'])
print(oddities([123]) == [123])
print(oddities([]) == [])

def oddities2(lst):
    result = []
    for (idx, item) in enumerate(lst):
        if idx % 2 == 0:
            result.append(item)
    return result

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities2([1, 2, 3, 4]) == [1, 3])
print(oddities2(["abc", "def"]) == ['abc'])
print(oddities2([123]) == [123])
print(oddities2([]) == [])