


# list of lists. each nested list contains two elements that represent the corresponding key/value pairs.
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car_list = []
for (key, value) in car.items():
    car_list.append([key, value])
    
print(car_list)