# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.
class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.studentClass = None

    def student_info(self):
        print("Student name is:", self.name)
        print("Student Id is:", self.id)
        print("Student class is:", self.studentClass)


Student1 = Student("Bruno", 14, )
Student1.studentClass = "Grate 3"
Student1.student_info()


# 2.Create a Vehicle class without any variables and methods
class Vehicle():
    pass


# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


vehicle = Vehicle(240, 5000)

print("My car Max Speed is: ", vehicle.max_speed)
print("My car Mileage is: ", vehicle.mileage)


# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Buss(Vehicle):
    def __init__(self, mileage, max_speed):
        super().__init__(mileage, max_speed)


schoolBuss = Buss(160, 15000)
print("School Buss max speed is: ", schoolBuss.max_speed)
print("School Buss mileage is: ", schoolBuss.mileage)


# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Buss(Vehicle, ):
    def __init__(self, max_speed):
        super().__init__(self, max_speed)
        self.capacity = None

    def seating_capacity(self,):
        print("Capacity buss is: ", self.capacity)


buss = Buss(Vehicle)
buss.capacity = 50
buss.seating_capacity()