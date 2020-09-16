#program to understand try, except and else block in python
#open the file it it exists and reads it.
#if not then exception block executes

filename = 'test.txt'
fd = None
try :
    print( "opening file ....",filename)
    fd = open(filename ,mode = 'r')
    print(filename ,"opens successfully")
    
except FileNotFoundError as ferr:
    print("File problem .. : ",ferr)
except Exception as err:
    print("Something went wrong ... ",err)

#execute only when error doesn't occur
else:
    print("file contents are : ")
    print(fd.read())
    fd.close()
    print(filename,"close success")
finally:
    print("Finally block executed ...")
