class Owner:
    def __init__(self, name):
        self.name = name 
        self.num_pets = 0
        
    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, name):
        self._name = name 
        
    def number_of_pets(self):
        return self.num_pets 
        
class Pet:
    def __init__(self, species, name):
        self.species = species 
        self.name = name 
        
class Shelter:
    def __init__(self):
        self.adopted_pets = {}

    def adopt(self, owner, pet):
        owner.num_pets += 1 
        if owner not in self.adopted_pets:
            self.adopted_pets[owner] = [pet]
        else:
            self.adopted_pets[owner].append(pet)
    
    def print_adoptions(self):
        for owner in self.adopted_pets:
            print(f'{owner.name} has adopted the following pets:')
            pets = self.adopted_pets[owner]
            for pet in pets:
                print(f'a {pet.species} named {pet.name}')
            print()
        

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")