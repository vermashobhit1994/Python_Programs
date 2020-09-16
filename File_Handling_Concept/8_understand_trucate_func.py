#program to understand truncate function in python

new_file_size = 20


filename = 'copy_file_to_be_read.txt'
with open(filename,mode = 'a') as fd:#here file must be opened in write or append mode
    fd.truncate(new_file_size)#make the sizeof the file to be 20 bytes
  
with open(filename) as fd:
    print(fd.read())
