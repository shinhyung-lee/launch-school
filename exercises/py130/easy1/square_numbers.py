nums = [1, 2, 3, 4, 5]

squared = list(map(lambda num: num**2, nums))
for num in squared:
    if num == 9:
        break 
    print(num)
    
print('first loop ended')

for num in squared:
    print(num)