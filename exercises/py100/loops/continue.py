cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities: 
    if city is None:
        pass 
    else:
        print(len(city))