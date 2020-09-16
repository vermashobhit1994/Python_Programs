#program to understand how we can raise an exception based on condition
#here if we try to open filename = 'corrupt_file.txt ' then raise an exception manually

filename = 'corrupt_file.txt'
try:
    fd = open(filename )
    if fd.name == 'corrupt_file.txt':
         raise Exception#raise general exception if trying to open corrupt_file.txt

except FileNotFoundError as ferr:
    print("file problem : ",ferr)

except Exception as err:
    print("Externally raised exception  ")

else:
    print("reading contents : ")
    print(fd.read())
    fd.close()

finally:
    print("finally block executed   ")
    


