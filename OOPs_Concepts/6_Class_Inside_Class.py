#Program to understand class inside class
#We can create the variable inside the outer class or outside the outer class.
#When creating a variable inside the outer class then use self
#When creating a variable outside the outer class use the outer class Name
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        #create a object of inner (Laptop) class inside the outer class
        #here lap is object for inner class. E.g for S1 ->  S1.lap = S1.Laptop() 
        self.lap = self.Laptop()

    def show_details(self):
        print(self.name,self.rollno)
        #to show the laptop details for student 
        self.lap.show_details()
    """ ####### CREATING A CLASS INSIDE MAIN CLASS#############"""
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        #method to show the details of the Laptop 
        def show_details(self):
            print(self.brand,self.cpu,self.ram)

#creating the objects
S1 = Student("shobhit",100)
S2 = Student("apukhote",200)

#printing the values
#1. By using the object Name
print("Display Student details by using object")
print(S1.name,S1.rollno)
print(S2.name,S2.rollno)
#2. By using the method
print("\nDisplay Student details by using method")
S1.show_details()
S2.show_details()

#print the inner class variables by using the outer class objects
print("Inner class variables by Outer class objects")
print(S1.lap.brand,end=' ')
print(S1.lap.cpu,end=' ')
print(S1.lap.ram)

#create the Inner class (Laptop) variables using the outer class objects
lap1 = S1.lap
lap2 = S2.lap

#print the address of inner class variables to check if they're different or not
print("\n\nPrinting the ID's of the inner class objects")
print(id(lap1))
print(id(lap2),"\n\n")

#print the inner class variables by using the inner class objects
print("Inner class variables by Outer class objects")
print(lap1.brand,end=' ')
print(lap1.cpu,end=' ')
print(lap1.ram)

print(lap2.brand,end=' ')
print(lap2.cpu,end=' ')
print(lap2.ram)

print("\n\n")


#create a object of inner class outside the outer class
lap1_outer = Student.Laptop()
lap2_outer = Student.Laptop()
print("Display details of inner class by variables created outside of outer class ")
lap1_outer.show_details()

print("\n\n")

#print  Outer and Inner class data since we're calling the inner class method
#inside the outer class method i.e show_details()
print("Details of Student Name, RollNO along with Laptop details")
S1.show_details()
