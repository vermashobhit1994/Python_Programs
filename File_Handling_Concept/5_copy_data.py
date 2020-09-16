#program to copy the data from one file to other 
#also we're going to understand tell() and seek() and seekable()
#file is seekable if it allow access to file stream e.g seek() method
#if I want to read a file backward I can do only if file opened in binary mode.
#input filename : file_to_be_read.txt
#output filename : copy_file_to_be_read.txt

input_filename = 'file_to_be_read.txt'
output_filename = 'copy_file_to_be_read.txt'

#open the inputfile
fd_input = open(input_filename ,mode = 'r')
#open the output file
fd_output = open(output_filename,mode = 'a')


""" ######################## done by using for loop i.e read all the file start ###########################################"""
for line in fd_input:#read line by line 
    print(line)
    fd_output.write(line) #write line with fd_output object

fd_output.write("\n\n") #done to separate the second time write

""" ######################## done by using for loop i.e read all the file ends ###########################################"""


if(fd_input.seekable()):#check if file is seekable or not
    print(input_filename,"is seekable")
    #move the file object to start of file
    fd_input.seek(0)
    fd_output.seek(0)
print("\n\n")#to provide separation

""" ######################## done by using while loop i.e read all the file start ###########################################"""


#read the  bytes  = no_of_bytes at time using while loop and then write it
no_of_bytes = 100
line_data = fd_input.read(no_of_bytes)

while(len(line_data) > 0):
    print(line_data,end ='')
    print('\ncurrent position = ',fd_input.tell())

    fd_output.write(line_data)
    line_data = fd_input.read(no_of_bytes)

fd_output.write('\n\n') #to separate the next time write

""" ######################## done by using while loop i.e read all the file ends ###########################################"""

fd_input.close()
fd_output.close()    

