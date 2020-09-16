#program to understand try except block


a = 10
b = 3

    

try :
     fd = open('test.txt',mode = 'w')#open the file resource
     print("file is opened")
     print(a/b)
     print("Division successful")#print only when no error otherwise go to exception 


#except execute only if we've an error to handle it.
except Exception as err:#here Exception is general error to handle any error
    print("error in dividing : ",err)

#execute only if no error
else: 
    print("Division is successfully done in else")

#this is used to close the resources or done the task which isn't done in both try and except block
finally: 
    fd.close()
    print("file is closed")


print("Statement will gets printed")#print the line always
    
