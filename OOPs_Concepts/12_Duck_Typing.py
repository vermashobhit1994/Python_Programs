#Program to understand Duck Typing in Python

class Pycharm:
    def execute(self):
        print("Compiling")
        print("running")

class Myide:
    #same method name as that of above class
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("running")

class Laptop:
    def code(self,IDE):
        IDE.execute()

#creating an object ide of Pycharm 
ide = Pycharm()
#printing the code ()
lap1 = Laptop()
lap1.code(ide)

print("\n\n")

#change to Myide class
ide = Myide()

#create object of Laptop class
lap2 = Laptop()
lap2.code(ide)