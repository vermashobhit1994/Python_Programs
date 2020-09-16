#program to understand append mode in python

filename = 'file_to_be_write.txt'
fd = open(filename,mode = 'a')
fd.write(input("Enter the data to append to file : "))
fd.close()

