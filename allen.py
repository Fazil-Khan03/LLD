'''
Your aim is to write a console program that can simulate a batch allocation system
Users have the following capabilities
 Students should be able to register to the system.
 Admin should be able to register to the system.
 Admin should be able to create the batches.
 Students should be able to enroll for a particular stream.
 A student can enroll only once in any stream(IIT/NEET).
 Admin should be able to allocate a batch to students on the basis of multiple criteria.
 Gender based
 Female students should be allocated in the below sequence .
 Morning -> Noon -> Evening i.e. if morning is available it should be
allocated first
○ Highest Capacity
 Biggest initial capacity batches should be allocated first.
 Batch allocation will happen to all the batches present in the system(created by any
admin) for a given stream.
Input and output
The inputs for various actions supported should be taken by invoking some method. The
method signature should contain sufficient information to support all the requirements.
You may change the input output format without changing the fu

'''

from abc import ABC, abstractmethod
from enum import Enum
class BatchSystem:

    def __init__(self) -> None:
        self.admins = []
        self.students = []
        self.batches = []
    
    def allocate_batches(self, student):
            all_batches = filter(lambda batch : batch.type == student.enrolled_stream , self.batches)
            if student.gender == 'Female':
                morning_batches = filter(lambda batch : batch.shit == 'morning' , self.all_batches)

            # find the biggest initial capacity
            high_cap_batch = None
            max_capacity = -1
            for batch in self.batches:
                if batch.capacity > max_capacity:
                    max_capacity = batch.capacity
                    high_cap_batch = batch
            student.allocated_batch = high_cap_batch
            high_cap_batch.capacity = high_cap_batch.capacity - 1


class BatchTime(Enum):
    morning = 1
    noon = 2
    evening  = 3

class Batch:

    def __init__(self, batch_id, type, start_time, shift, capacity) -> None:
        self.batch_id = batch_id
        self.type = type,
        self.start_time = start_time 
        self.shift = shift
        self.capacity = capacity


class Person:

    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, roll_no, name,  gender, dob, enrolled_stream) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.dob = dob
        self.enrolled_stream = enrolled_stream
        self.allocated_batch = None

class Admin(Person):

    def __init__(self, admin_id, name,  gender, dob) -> None:
        self.batch_systen = None
        self.roll_no = admin_id
        self.name = name
        self.gender = gender
        self.dob = dob
    
    def register_admin(self, batch_sysem):
        self.batch_systen = batch_sysem
    
    def allocate_batch(self, student):
        self.batch_systen.allocate_batches(student)
    
    def create_batches(self, batch):
        self.batch_systen.batches.append(batch)


batch_system  = BatchSystem()
admin = Admin('123', 'Fazil', 'M', '23-12-2023')
admin.register_admin(batch_system)

# create student

fazil = Student("1", 'Fazil', 'Male', '1990-09-01', 'IIT')
ashraf = Student("2", 'Ashraf', 'Male', '1998-09-01', 'NEET')
adil = Student("3", 'Adil', 'Male', '1996-09-01', 'NEET')


batch1 = Batch("1", "IIT", '10:00', 'Morning', 100)
batch2 = Batch("2", "NEET", '10:00', 'Morning', 100)
batch3 = Batch("3", "IIT", '12:00', 'Noon', 100)

batch4 = Batch("4", "NEET", '06:00', 'Evening', 40)
batch5 = Batch("5", "IIT", '06:00', 'Evening', 40)

admin.register_admin(batch_system)
admin.create_batches(batch1)
admin.create_batches(batch2)
admin.create_batches(batch3)
admin.create_batches(batch4)
admin.create_batches(batch5)
admin.allocate_batch(fazil)


print("Student name {}, roll no {}, batch {} shift {}".format(fazil.name, fazil.roll_no, fazil.allocated_batch.batch_id, fazil.allocated_batch.shift))
print("Student name {}, roll no {}, batch {} shift {}".format(fazil.name, fazil.roll_no, fazil.allocated_batch.batch_id, fazil.allocated_batch.shift))


    
        