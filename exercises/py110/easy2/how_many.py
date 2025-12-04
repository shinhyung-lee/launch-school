'''

Input: A list of vehicles
Output: None. Inside the function, function prints out the number of occurrences of each element
        from the input vehicle list.

Rules
Explicit:
    - words are case sensitive ('suv' != 'SUV')
Implicit:

Data Structures:
    - Dictionary 

Algorithms:
    - initialize an empty dictionary "vehicle_frequency"
    - iterate each element in the "vehicles" list
        - if the vehicle is NOT in the list, initialize key-value pair for the vehicle in "vehicle_frequency"
            - vehicle_frequency[vehicle] = 0
        - increment the value for vehicle
            - vehicle_frequency[vehicle] += 1
    - iterate through "vehicle_frequency" dictionary
        - print out each vehicle and its occurrences
        - "vehicle" => "occurrence"
'''

# Method 1
def count_occurrences(vehicles):
    vehicle_frequency = {}
    for vehicle in vehicles:
        if vehicle not in vehicle_frequency:
            vehicle_frequency[vehicle] = 0

        vehicle_frequency[vehicle] += 1
    for vehicle, occurrence in vehicle_frequency.items():
        print(f"{vehicle} => {occurrence}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# Method 2
def count_occurrences2(vehicles):
    counter = {} 

    for vehicle in vehicles:
        counter[vehicle.casefold()] = counter.get(vehicle.casefold(), 0) + 1 
    
    for item, count in counter.items():
        print(f"{item} => {count}")


vehicles2 = ['car', 'CAR', 'truck', 'CaR', 'SUV', 'trUCk',
            'motorcycLe', 'motORcycle', 'cAr', 'Truck']

count_occurrences2(vehicles2)
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2