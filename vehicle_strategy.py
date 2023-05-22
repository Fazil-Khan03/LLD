from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    
    @abstractmethod
    def drive(self):
        pass

class NormalDriveStrategy(DriveStrategy):

    def drive(self):

class Vehicle:
    pass

    