#!/usr/bin/env python3
#specify that the python interpreter is used and we can run program directly i.e
#by using the ./filename
 

#Program to understand socket programming in python using the server program
import socket
HOST_ADDR = ''#this must be a numeric address if other than localhost(127.0.0.1)
PORT_NO = 65534#valid range is >1024 to 65535 since <1024 are reserved 
BUFFER_SIZE = 1024#buffer for received data i.e 1KB


#AF_INET for the Internet address family IPv4
#SOCK_STREAM specify the TCP/IP Protocol for the socket
#create and open a socket object of given type 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
    print("Socket created")
    #bind the socket with specific network and Port No.
    #since we're using the IPv4 address family so bind accepts a tuple of hostaddress
    #and port no
    #if argument is empty then accept all connections from the IPv4 address clients
    soc.bind((HOST_ADDR,PORT_NO))
    #enable to accept the connections i.e make it a listening socket.
    #10 specify the max no of clients at one time to connect.
    #if not specify then max value is 128(Path : /proc/sys/net/core/somaxconn)
    soc.listen(10)
    print("waiting for clients......")
    #accept blocks and wait for client to connect.
    #for IPV4 return a new socket connection object and tuple i.e (host,port) for address of client. 
    #this new connection object i.e conn_obj is different from object where the 
    #server is listening i.e soc object. 
    conn_obj,addr_client = soc.accept()
    with conn_obj:
        #print("Connected to : ",conn_obj)#print the socket object contents
        print("Connected to address :",addr_client)
        #infinite loop to receive what the client has sent
        while True:
            #recv return an empty string if remote end is closed connection.
            #blocks until data is received.Here the data received is bytes string
            data_recv = conn_obj.recv(BUFFER_SIZE)
            
            
            #if an empty bytes string is received that means client has closed the connection
            if not data_recv:
                break#break out of infinit loop
    
            #print the received data
            print("Received data : ",data_recv.decode())
            
            #send the data received to client again.
            #it returns the no of bytes sent
            nbytes_send = conn_obj.sendall(data_recv)

            #print the no of bytes sent
            print("bytes sent {} ".format(nbytes_send))
            
            



