#Program to understand Method overloading in python
class A:
    def show(self):
        print("in Class A show function")

#class B inherit from class A
class B(A):
    #method override the show function in class A
    #if the below comment then print the class A show()
    def show(self):
        print("In class B show function")    
    pass

#create a class A object
a1 = A()
#create a class B object
b1 = B()

#print the show of the class A 
a1.show()
b1.show()#print the class B show function.