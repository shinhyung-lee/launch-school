
class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100 
        self.weapon = weapon 
        
    def __str__(self):
        return f'Naem: {self.name}, Health: {self.health}'

    def attack(self, other):
        other.health -= self.weapon.weapon_damage
        
class Warrior(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
        self.stamina = 100 
        
    def attack(self, other):
        if self.stamina < 10:
            print("Not enough stamina to attack.")
        else:
            self.stamina -= 10
            super().attack(other)
        

class Mage(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
        self.mana = 100 
        
    def cast_spell(self, target):
        if self.mana < 20:       
            print("Not enough mana to cast spell.")
        else:
            self.mana -= 20
            super().attack(target)
            super().attack(target)
    
class Weapon:
    def __init__(self, name, weapon_damage):
        self.name = name 
        self.weapon_damage = weapon_damage
        
    def __str__(self):
        return f'Weapon: {self.name}, Damage: {self.weapon_damage}'
    
sword = Weapon("Sword", 15)
staff = Weapon("Staff", 8)
fists = Weapon("Fists", 5)

aragorn = Warrior("Aragorn", sword)
gandalf = Mage("Gandalf", staff)
goblin = Character("Goblin", fists)

print(aragorn.weapon)  # Expected: Weapon: Sword, Damage: 15
aragorn.attack(goblin)
print(goblin)          # Expected: Name: Goblin, Health: 85

gandalf.attack(goblin)
print(goblin)          # Expected: Name: Goblin, Health: 77