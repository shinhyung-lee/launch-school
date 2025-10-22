
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(dest: str, travel_list: list) -> bool: 
    '''
        Given dest (destination) and travel_list (a list of cities), if dest is included in travel_list,
        function returns True. Otherwise, return False.
    '''
    if type(travel_list) is not list:
        return False 
    for city in travel_list:
        if city == dest:
            return True 
    return False 

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False