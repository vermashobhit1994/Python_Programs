#program to understand open function in python with modes

fd = open("file_to_be_read.txt",mode = 'r')#here the filename "file_to_be_read" is opened in read mode.
print(fd)#print the file object with name , mode and encoding
print("filename = \"",fd.name,"\"")#print the filename
print('mode = \'',fd.mode,'\'')#print the filemode
fd.close()#closing file using file object
