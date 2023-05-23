'''
Author : Fazil Khan
Date : 23 May, 2023

'''

from abc import ABC, abstractmethod

class WeightMachine(ABC):

    @abstractmethod
    def get_weight_pound(self):
        pass

class WeightMachineForBabies(WeightMachine):

    def get_weight_pound(self):
        return 28 # return weight of babies

class WeightMachineAdapter(ABC):

    @abstractmethod
    def get_weight_kg(self):
        pass


class WeigthMachineAdapterImp(WeightMachineAdapter):

    def __init__(self, weight_machine) -> None:
        self.weight_machine = weight_machine
    
    def get_weight_kg(self):
        weight_kg = self.weight_machine.get_weight_pound()
        return weight_kg * .45

if __name__ == "__main__":
    weight_machine  = WeightMachineForBabies()
    weight_machine = WeigthMachineAdapterImp(weight_machine)
    print(weight_machine.get_weight_kg())