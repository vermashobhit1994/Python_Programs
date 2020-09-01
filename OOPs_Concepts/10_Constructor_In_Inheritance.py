#Program to understand how constructor or __init__() is called in multiple inheritance
#This is done in order in which class is inherited .
#Here we also understand use of super() i.e to access the parent class
class B:
    #by the creation of class B constructor it will call it instead of class A
    def __init__(self):
        #super().__init__()#To access the class A init method 
        print("In Class B Init function")
    #property 1 function is common in both class A and class B
    def property1(self):
        print("Inside the Class B Property 1")
    def property4(self):
        print("Inside the Class B Property 4")

class A:
    def __init__(self):
        print("In Class A Init function")
    #property 1 function is common in both class A and class B
    def property1(self):
        print("Inside the Class 1_A Property 1")
    def property2(self):
        print("Inside the Class A Property 2")
        
#if in below class inheritance we change the order from (B,A) to (A,B) then
#class A will become the super class first for child class C.
class C(B,A):
    def __init__(self):
        print("In Class C Init function")
        #calling the super class __init__() .
        #here the super class is chosen according to order in which classes are inherited
        #here since B is inherited first so it will call the init() of class B
        super().__init__()

    def feat(self):
        super().property1()#access the super class method by super() i.e the class B    

#creating the object of Class A
a1 = A() #call the class A __init__()
print("\n\n")

#creating the object of Class B
b1 = B()# call the class B __init__()

print("\n\n")

#creating the object of Class C
c1 = C() #call the __init__() of class C and Class B
c1.property1()#call the property1() of class B

print("\n\n")
c1.feat()#call the property1() of class B by use of super()
