#program to handle multiple error 
#here we're handling ZeroDivisionError and ValueError
#if other than above then handled by Exception Error

a,b = map(int,input("enter the two values : ").split())

try: 
    fd = open('test.txt')#open the resource if success execute next line otherwise goto 
    
    print("test.txt opened ")
    print(a/b)
    data_int = int(input("enter a number :" ))
    print(data_int)
    
except ValueError as verr:#error handling on invalid input by user
    print("Incorrect Input : ",verr)

except ZeroDivisionError as zerr:#error handling on zero division
    print("Divide by zero :",zerr)

#here it will print the file Error if occurs
except Exception as err:#general error handling.Done at last to handle if none of above error occuring
    print("Something went wrong ....  ",err)

finally:#to close the resources allocated
    fd.close()
    print("close the test.txt file ")
 

 
    
