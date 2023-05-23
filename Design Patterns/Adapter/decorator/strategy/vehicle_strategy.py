from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    
    @abstractmethod
    def drive(self):
        pass

class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal Drive strategy")

class SpecialDriveStrategy(DriveStrategy):

    def drive(self):
        print("Special Drive strategy")

class Vehicle:

    def __init__(self, drive_request) -> None:
        self.drive_request = drive_request
    
    def drive(self):
        self.drive_request.drive()

class SportVechicle(Vehicle):
    pass

class NormalVehcile(Vehicle):
    pass


# sport vechicle

sport_vehcile = SportVechicle(SpecialDriveStrategy())
sport_vehcile.drive()

normal_vehcile = SportVechicle(NormalDriveStrategy())
normal_vehcile.drive()



    