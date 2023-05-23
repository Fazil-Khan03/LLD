from abc import ABC, abstractmethod

class EmployeeDAU(ABC):
    
    @abstractmethod
    def create(self, client, employee_obj):
        pass

    @abstractmethod
    def delete(self, client, employee_id):
        pass

    @abstractmethod
    def get(self, employee_id):
        pass

class EmployeeImp(EmployeeDAU):

    def create(self, client, employee_obj):
        print('created a new row in the employee table')
    
    def delete(self, client, employee_id):
        print('deleted the row in the employeee table')
    
    def get(self, client, employee_id):
        print("fected row in the employee table")
        return EmployeeDAU()

class EmployeeDauProxy(EmployeeDAU):
    
    def __init__(self) -> None:
        self.employee_dau = EmployeeImp()
    
    def create(self, client, employee_obj):
         
         if (client == 'ADMIN'):
             self.employee_dau.create(client, employee_obj)
         else :
             raise Exception("Access denied")
    
    def delete(self, client, employee_id):
         
         if (client == 'ADMIN'):
             self.employee_dau.create(client, employee_id)
         else :
              raise Exception("Access denied")
    
    def get(self, client, employee_id):
        if client == 'ADMIN' or client == 'USER':
           return  self.employee_dau.get(client, employee_id)
        else:  raise Exception("Access denied")
             
if __name__ == '__main__':
    request = EmployeeDauProxy()
    request.create('ADMIN', EmployeeImp())
    # request.create("user", EmployeeImp()) #raise exception
    # request.get("user", '123'))

    








