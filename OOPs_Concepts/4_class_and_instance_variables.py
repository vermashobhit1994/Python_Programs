#Program to understand Class and Instance Variables
#here change on instance variables only change that object variable
#here change on Class variables changes on all objects 
class Car:
    #class variable
    wheels = 4
    
    def __init__(self):
        #MILEAGE and company are instance variables
        self.MILEAGE = 10
        self.company = "BMW"
    
#creating the objects
car1 = Car()
car2 = Car()

""" ############### INSTANCE VARIABLES CONCEPT #############################"""
#changing the MILEAGE of car1
car1.MILEAGE = 8

#print the instance variables
#here the MILEAGE i.e instance variabe gets changed
print(car1.MILEAGE,car1.company)#Change to particular object only
print(car2.MILEAGE,car2.company)


""" ############### CLASS VARIABLES CONCEPT #############################"""
#print the class variables
print("Class variables print by object name ")
print(car1.wheels)
print(car2.wheels)
print("\nClass variables print by Class name ")
print(Car.wheels)


#changing the class variable.Here change for both the objects.
Car.wheels = 5
print("After modification Class variables print by object name ")
print(car1.wheels)
print(car2.wheels)
