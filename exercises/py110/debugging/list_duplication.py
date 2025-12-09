

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
seen = set() 

for idx, value in enumerate(data):
    if value not in seen:
        unique_data.append(value)
        seen.add(value)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed