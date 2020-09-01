#Program to understand self in class
#Here we also understand how to change the current instance variable value

class Computer:
    def __init__(self):
        self.name = "shobhit"
        self.age = 30
    def update(self):
        self.age = 60

    def compare_age(self,other):
        if(self.age == other.age):
            return True
        else:
            return False

#creating the objects
#Here Computer() is constructor which is used to allocate memory to object.
#The size of memory is depends on no of variables inside object and size of each variable.
com1 = Computer()
com2 = Computer()

#printing the address of objects.Here the address is different
print(id(com1))
print(id(com2))

"""############## CHANGING THE CURRENT INSTANCE VALUE BY USING OBJECT #############################"""
#change the name of com1 object
com1.name = "apukhote"

"""############## CHANGING THE CURRENT INSTANCE VALUE BY USING METHOD #############################"""
#change the age of com1 object using update()
#If comment below statement then print the same age at last
com1.update()

#print the same name since we're assign to current object inside the class 
print(com1.name)#name changes from "shobhit" to "apukhote"
print(com1.age)#age changes from 30 to 60
print(com2.name)#name remains to "shobhit"

"""################### UNDERSTAND SELF ##########################################"""
"""here the com1 goto self in compare_age()while the com2 go to other variable of function"""
#compare_age return true if age is same otherwise false
if com1.compare_age(com2):
    print("Both object have same age")
else:
    print("Both object have different age")