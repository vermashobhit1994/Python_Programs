#program to understand different functions while reading a file


filename = 'file_to_be_read.txt'



""" ################################## Understand read() start #######################################################"""
fd = open(filename)#open file in read mode(default case) 
file_data = fd.read(14)#read 14 characters only. If not specify any value then read entire file
print(file_data,end = '')#here newline after reading all contents from file . to avoid use end
fd.close()
""" ################################## Understand read() ends #######################################################"""

print("\n\n")

""" ################################## Understand readline() start ##############################################"""
fd = open(filename)
line_data = fd.readline()#read 1st line only
print(line_data)
line_data = fd.readline(11)#read only the 11 characters of second line
print(line_data)
fd.close()
""" ################################## Understand readline() ends  ##############################################"""


""" ################################### understand readlines() start ##############################################"""
fd = open(filename)
lines_data = fd.readlines()#read the whole file in list with '\n'
print(lines_data)

fd.seek(0)#to move the pointer to beginning of file after reading all contents
print('\n\n')

lines_data = fd.readlines(0)#read whole file in form of list of elements
print(lines_data)

fd.seek(0)#to move the pointer to beginning of file after reading all contents
print('\n\n')

#if no of bytes of line exceed the specified value in readlines() then print that line since it's a list.
lines_data = fd.readlines(1)#if >0 then print first line.  
print(lines_data)

fd.seek(0)#to move the pointer to beginning of file after reading all contents
print('\n\n')

#print the lines of file until  no of bytes of first line is less than the specified value in readlines().
lines_data = fd.readlines(45)#first line contains the 23 characters so it will print second line also.
print("characters = ",len(lines_data[0]))#read the no of character in first line
print(lines_data)
fd.close()

""" ################################# Understand readlines() ends###########################################"""



""" ################################## Understand readable() start #######################################################"""
fd = open(filename)
if( fd.readable() ):#returns true if file is readable else false.NOt take any arguments
    print("file is readable")
else:
    print("file isn't readable")

fd.close()

""" ################################## Understand readable() ends  #######################################################"""
