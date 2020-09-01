#program to understand how we can initialize the object with values upon creation
class Computer:
    def __init__(self,cpu,ram):
        print("object created")
        self.CPU = cpu#here the cpu is local variable while the CPU is current instance variable
        self.RAM = ram#here the ram is local variable while the RAM is current instance variable
    def Config(self):
        print("Current Config is ",self.CPU,self.RAM)
"""creating the objects"""
#creating the object with i5 as processor value and 16 gb as ram value
com1 = Computer('i5',16)#here com1 is passed to __init__() self argument by default

#creating the object with i3 as processor value and 8 gb as ram value
com2 = Computer('i3',8)#here com1 is passed to __init__() self argument by default

#calling the Config function
com1.Config()#here the com1 is passed as argument to self in Config()
com2.Config()#here the com2 is passed as argument to self in Config()