#Program to understand how we can call the function inside a class.
#1. By using class name and then passing the object name as paramter
#2. By using the object name itself
class Computer():
    def Config(self):
        print("i5,16gb,1TB")

#creating the object.
#here the __init__() is called default with com1 as argument i.e
#com1 = Computer(com1). This com1 in argument is passed to __init__()
com1 = Computer()
com2 = Computer()

#Calling by Class Name
print("Calling by Class Name")
Computer.Config(com1)
Computer.Config(com2)

print("\n")#to provide the separation

#Calling by Object
print("Calling by object")
com1.Config()
com2.Config()