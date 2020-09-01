#Program to understand Method overloading in python
class Student:
    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    #Implement the Method Overloading
    def add_marks(self,marks1 = None,marks2 = None,marks3 = None):
        #if 3 arguments are passed
        if marks1 != None and marks2 != None and marks3 != None: 
            sum = marks1 + marks2 + marks3
        #if only 2 arguments are passed
        elif marks1 != None and marks2 != None:
            sum = marks1 + marks2
        #if only 1 argument is passed
        else:
            sum  = marks1
        
        return sum
        

    

#create a object 
S1 = Student(45,78)

print(S1.add_marks(34))
print(S1.add_marks(10,20))
print(S1.add_marks(10,20,30))
