#
# CPSC-471 Assignment 1
# Joseph Haddad
#
# Add various socket calls in various places, as required.
# Just a hint, see the sample TCPServer.py in the book
#
# Disclaimer:  There are no guarantees that the comments or
#              the code in this file are very accurate
#

#import socket module
from socket import *
import sys                       # In order to terminate the program

# Create a TCP server socket
# AF_INET is used for IPv4 protocols
# SOCK_STREAM is used for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Fill in start
serverPort = 8080                                
serverSocket.bind(('', serverPort))              
serverSocket.listen(1)                            
#Fill in end

while True:
    #Establish the connection
    #Fill in start
    connectionSocket, addr = serverSocket.accept()    
    #Fill in end      
    print('Ready to serve...')

    try:        
        #Fill in start
        message =  connectionSocket.recv(1024)
        #Fill in end

        filename = message.split()[1]                          
        f = open(filename[1:])
       
        #Fill in start
        outputdata = f.read()

        #Fill in end

        #Send one HTTP header line into socket
        #Fill in start
        httpHeader = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(httpHeader.encode())
        #Fill in end


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found            
        #Fill in start
        connectionSocket.send("Error 404: File Not Found\r\n".encode())
        #Fill in end

        #Close client socket                                
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()

sys.exit()        #Terminate the program after sending the corresponding data