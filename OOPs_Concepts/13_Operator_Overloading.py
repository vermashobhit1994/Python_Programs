#Program to understand how operator can be overload to do function what we want.
""" behind the scene the special method i.e __add__() is called when you use
'+' operator.
a = '5'
b = '6'
print(a+b)
#add is special method to the int class
#print(int.__add__(a,b))
print(str.__add__(a,b)) #output is 56
"""


class Student:
    def __init__(self,m1,m2) :
        self.m1 = m1
        self.m2 = m2
    
    #method that will called once '+' is used
    #here we're changing the behaviour of method by overloading it
    def __add__(self,other):
        #add the m1 marks of both the objects
        m1 = self.m1 + other.m1
        #add the m2 marks of both the objects
        m2 = self.m2 + other.m2
        #create a new object name as s3 with updated value of m1 and m2 
        #after adding above
        s3 = Student(m1,m2)
        return s3#return the newly created object with modified values
    
    #called when we use '>' operator
    def __gt__(self,other):
        #add the m1 marks of both the objects
        res1 = self.m1 + other.m2
        #add the m2 marks of both the objects
        res2 = self.m2 + other.m2
        #here res1 and res2 are just variables
        if res1 > res2:
            return True
        else:
            return False
    #overloading the method i.e called when we print any object to display
    #value instead of the result is module name, class name ,object address. 
    """ COMMENT THE BELOW FUNCTION TO PREVENT OVERLOAD"""
    def __str__(self):
        #use the .format to return the string instead of tuple i.e the default return type
        return "{}, {}".format(self.m1,self.m2)


#creating the two objects
S1 = Student(90,78)
S2 = Student(12,15)

# below converted to Student.__add__(S1,S2) i.e className.funcName(Parameters)
#S1 goes to self and S2 goes to other in function __add__()
S3 = S1 + S2
print(S3.m1)
print(S3.m2)

#Compare the marks for two objects
if S1 > S2:
    print("S1 wins")
else:
    print("S2 wins")

#__str__() is called when we print any object
#its result is module name, class name ,object address
a = 10
print(a)
print(a.__str__())#here print the value instead of object name with address
#print the S1

#After overloading the __str__()
print(S1)
print(S1.__str__())



