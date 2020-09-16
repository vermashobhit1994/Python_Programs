#program to understand writing functions 

#filename = input("enter name of file : ") -> commented since hard coded filename
filename = 'file_to_be_write.txt'


fd = open(filename,mode = 'w')
input_data = input("Enter data to be written : ")
fd.write(input_data)
fd.write("extra line written")
fd.close()


#understand writelines()
fd = open(filename ,mode = 'w')

input_list = []

input_list.append( input("Enter data :"))#take the input data and then append to input_list empty list
input_list.append(input("enter data : "))
fd.writelines(input_list)#write the input_list to file
fd.close()


""" ######################## Understand writeable() start ##################################################### """
#understand writable function
#fd = open(filename,mode = 'w')

#print(fd.writeable())#function isn't working in python 3.5v

"""
if(fd.writeable()):
    print("file is writeable")
else: 
    print("file isn't writeable")
"""
fd.close()

""" ######################## Understand writeable() ends ##################################################### """

