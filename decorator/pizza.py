from abc import ABC, abstractmethod

class BasePizza(ABC):

    @abstractmethod
    def cost(self):
        self

class FarmHouse(BasePizza):

    def cost(self):
        return 200

class VegDelight(BasePizza):

    def cost(self):
        return 100

class Margherita(BasePizza):

    def cost(self):
        return 300

class ToppingDecorator(BasePizza):
    pass

class ExtraCheese(ToppingDecorator):

    def __init__(self, base_pizza) -> None:
        self.base_pizza = base_pizza
    
    def cost(self):
        return self.base_pizza.cost() + 10

class Mushroom(ToppingDecorator):

    def __init__(self, base_pizza) -> None:
        self.base_pizza = base_pizza
    
    def cost(self):
        print(self.base_pizza.cost() + 20)

if __name__ == '__main__':

    # now i need margherita and extra cheese
     pizza = ExtraCheese(Margherita())
     pizza.cost()

     pizza = Mushroom(ExtraCheese(Margherita()))
     pizza.cost() #mushroom plus extra cheeze plus margherita
 


