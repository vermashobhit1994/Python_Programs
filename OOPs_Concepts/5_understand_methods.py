#Program to understand different methods used in Class 
#for the instance method the variable can be anything instead of self
#for the class method the variable can be anything instead of cls but must use @classmethod decorator
#for the static method neither class variable nor instance variable isn't required but use @staticmethod decorator
class Student:
    school_name = "shobhitverma"
    def __init__(self,m1,m2,m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
    """ ############ INSTANCE METHOD CONCEPT START ##################"""    
    #Instance Method since we're using the current instance i.e self
    def find_avg(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

    #accessor or get method to get the value of variable
    def get_marks1(SELF):
        return SELF.marks1#here the self changes to SELF 
    #Mutator or set method to modify the value of variable
    def set_marks1(self,value):
        self.marks1 = value
    """ ############ INSTANCE METHOD CONCEPT ENDS ##################"""    
    
    """ ############ CLASS METHOD CONCEPT START ##################"""    
    #class method
    #decorator so that the class method can be called without providing 
    #object name inside the parameter and convert the method to class method.
    @classmethod
    def get_school_name(class_Name):
        return class_Name.school_name
    """ ################## CLASS METHOD CONCEPT ENDS ###########"""
    
    """ ################## STATIC METHOD CONCEPT START ###########"""
    #static method
    #decorator so as to specify that it is static method 
    #this method takes no arguments i.e className or self 
    @staticmethod
    def info_class():
        print("This is the Student Class")
    """ ################## STATIC METHOD CONCEPT ENDS ###########"""




#creating the objects i.e students
s1 = Student(10,20,30)
s2 = Student(78,45,23)

""" ############ INSTANCE METHOD CONCEPT START ##################"""

#calling the instance method i.e find_avg
print(s1.find_avg())
print(s2.find_avg())

#getting the values 
#printing by using the objects
print(s1.marks1)
#setting the values i.e modify the values by using the setter method
print("Modify the marks1 for both objects")
s1.set_marks1(52)
s2.set_marks1(85)
#Getting the value by using the getter method
print("getting the modified marks for both objects")
print(s1.get_marks1())
print(s2.get_marks1())

""" ################## INSTANCE METHOD CONCEPT ENDS ###########"""

""" ################## CLASS METHOD CONCEPT START ###########"""
#Access the class Method by using the instance variable
print(s1.get_school_name())
#Access the class Method by using the Class Name
print(Student.get_school_name())
""" ################## CLASS METHOD CONCEPT ENDS ###########"""

""" ################## STATIC METHOD CONCEPT START ###########"""
s1.info_class()
""" ################## STATIC METHOD CONCEPT ENDS ###########"""
