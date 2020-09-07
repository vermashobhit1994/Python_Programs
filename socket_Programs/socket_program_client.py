#!/usr/bin/env python3

#specify that the python interpreter is used and we can run program directly i.e
#by using the ./filename
#!/usr/bin/env python3

#Program to understand socket program in client side
import socket

HOST_ADDR = '127.0.0.1'
PORT_NO = 65534
BUFFER_SIZE = 1024

#create a socket object 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
    print("Socket created")
    #connect the socket object to remote address.
    #for IPv4 it is tuple of hostaddress and port no 
    soc.connect((HOST_ADDR,PORT_NO))
    
    """ ############ Here we're first sending user data and then a string ###########"""
    #input the data to be send
    data_send = input("Enter the data to be sent : ")
    
    #convert the string to byte string of 'utf-8' encoding technique.
    #this encoding technique can be 'ascii' also
    data_send_bytes = bytes(data_send,'ascii')
    
    #send the data input from user
    #here no error checking
    nbytes_send = soc.sendall(data_send_bytes)
    print("nbytes sent : ",nbytes_send)
    
    data_recv = soc.recv(BUFFER_SIZE)
    #decode() to convert the binary string to string
    print("Received data in socket : ",data_recv.decode())


    nbytes_send = soc.sendall(b'hello world')
    print("nbytes sent : ",nbytes_send)

    data_recv = soc.recv(BUFFER_SIZE)
    print("Received data in socket : ",data_recv.decode())

    
    
#print the received data .
#here the received data is converted to printable string using the repr() 
print("\n\nReceived data : ",data_recv.decode())