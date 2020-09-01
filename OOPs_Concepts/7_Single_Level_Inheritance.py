#Program to understand Single Level Inheritance
class A:
    def property1(self):
        print("Inside the Class A Property 1")
    def property2(self):
        print("Inside the Class A Property 2")

#class B inherit the class A       
class B(A):
    def property3(self):
        print("Inside the Class B Property 3")
    def property4(self):
        print("Inside the Class B Property 4")
    
#creating the object of Class A
prop1_A = A()

#creating the object of Class B
prop1_B = B()

#Access the method of class A as well as Class B by class B object
prop1_B.property1()
prop1_B.property2()
prop1_B.property3()
prop1_B.property4()

print("\n\n")

#Access the method of class A only by class A object
prop1_A.property1()
prop1_A.property2()
#prop1_A.property3()  #gives error
#prop1_A.property4()  #gives error
