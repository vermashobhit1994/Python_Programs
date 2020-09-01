#Program to understand the decorators in python using the div function .
#adding the extra functionality to original div function.
"""
Steps followed:
1. We're first updating the address of new function i.e inner_func to a new 
variable i.e div1 by calling the smart_div function.
2. Then we call the new function i.e inner_func with same parameters as original
function.
Here we're first checking whether first value is less than second value or not.
If yes then we swap the both.
3. Once the values updated then we call the original function with the values
and then stop the execution to return to function call.
"""

def div(a,b):
    print("inside the original div with address : ",div)
    print(a/b)

def smart_div(func):
    #func stores the address of above div function
    print("inside the smart_div with func ",func)
    #here the no of parameters must be same as that of div()
    #function that will add extra functionality
    def inner_func(a,b):#here the inner_func(a,b) becomes div(a,b)
        print("inside the inner_func") 
        if a < b:
            a,b = b,a
        print("inner_func address :",inner_func)
        print("smart_div address : ",smart_div)
        #return is used to return the original function i.e div return value
        #and stop the execution here.
        return func(a,b)#calling the original div with a,b as parameters i.e div(a,b)
    print("outside the inner_func")#execute first time when changing the address
    return inner_func

#here we're modifying the address of the original function(div) by new functionality
#function (inner_func).
#so div1 will store the address of inner_func
div1 = smart_div(div)
print("div1 address after first call :",div1)

print("\n\n")

#div1 stores the address of inner_func. Calling the inner_func by parameters
div1(2,4)
print("div address after second call ",div1)
