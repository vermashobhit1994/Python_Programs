#Program to understand Abstraction concept in python using the abstract class

#abc means abstract base classses
#import the abc for the abstract class implement
from abc import ABC,abstractmethod

#computer class is now a subclass of ABC class
class Computer(ABC):
    #abstract method since it has declaration but not definition of function
    @abstractmethod#comment this to allow the creation of object but then the class can't be called as abstract class
    def process(self):
        #print("Running") Comment so as to become a abstract class
        pass

#if we create a child class of abstract class then we need to give the definition
#of the abstract method i.e process() otherwise this new class (Laptop)
#also behaves as the abstract class 
class Laptop(Computer):
    #abstract method definition
    def process(self):
        print("Process is running in Laptop class")    
    pass

class Programmer:
    def work(self,com1):
        print("Solving the bugs problem")
        com1.process()

#if this class inherit the Computer class then process() must be there since 
#this behaves as abstract class so no object would be created.
#we haven't implement process method due to design aspect.
class Whiteboard():
    def write(self):
        print("I am writing")
        

#we can't create the object once we've used the ABC module      
#C1 = Computer() 
#C1.process()

#create an object of Laptop class
lap1 = Laptop()
lap1.process()

print("\n\n")
#create an object of Programmer class
prog1 = Programmer()
prog1.work(lap1)#passing the object of Laptop class

#create an object of Whiteboard class
w1 = Whiteboard()
prog1.work(w1)#passing the object of Whiteboard class