from abc import ABC, abstractmethod
class Character(ABC):
    
    def __init__(self,name, weapon):
        self.name = name
        self.weapon = None
        
    @abstractmethod
    def show_skill(self):
        pass
    
    @abstractmethod
    def change_weapon(self):
        pass

class King(Character):
    
    def __init__(self, name):
        self.name = name
     
    def show_skill(self):
        print(self.name,' King can move in all direction')
    
    def weapon_holding(self):
        print("King is holding", self.weapon.name)
        self.weapon.weapon_info()
        
    def change_weapon(self, weapon):
        self.weapon = weapon
    
        
class Queen(Character):
    
    def __init__(self, name):
        self.name = name
    
    def show_skill(self):
        print(self.name,' Queen can move in Straight/Diagonal direction')


class Weapon(ABC):
    
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def weapon_info(self):
        pass

class Knife(Weapon):
    
    def weapon_info(self):
        print("it can cause damage")

class Revolver(Weapon):
    
    def weapon_info(self):
        print("it can cause large  damage")

class Bazooka(Weapon):
    
    def weapon_info(self):
        print("it can wipe out people from existence")        
        

    
obj = King("Thomas")
obj.change_weapon(Revolver("Re-12XC"))
obj.change_weapon(Revolver("Kni-13XC"))
obj.show_skill()
obj.weapon_holding()

    