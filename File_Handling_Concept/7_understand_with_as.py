"""program to understand with...as i.e context manager, which are used to automatically release the resources used by file 
   in python.
This is mainly used in : a) closing the file automatically if an error encounter
                          b) close the unmanaged resources automatically if exception occurs

"""

filename = 'file_to_be_read.txt'
with open(filename,mode = 'r') as fd:#here closing of fd automatically
    print(fd.read(100))


