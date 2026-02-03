nums = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]

# nested generator expressions to create a flat list of nubmers
flat_list = list((num 
                  for sublist in nums 
                  for num in sublist))

print(flat_list)