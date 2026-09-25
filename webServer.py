# import socket module
from socket import *
# In order to terminate the program
import sys
from datetime import datetime



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("0.0.0.0", port))
  
  #Fill in start
  serverSocket.listen(5)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    response_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
    
    try:
      message = connectionSocket.recv(1024) #Fill in start -a client is sending you a message   #Fill in end 
      file = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(file[1:], "rb")     #fill in start              #fill in end
      
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      status = b"HTTP/1.1 200 OK\r\n"
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      out = b"Content-Type: text/html; charset=UTF-8\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      out += b"Server: CS-GY6843-WebServer\r\n"
      out += f"Date: {response_date}\r\n".encode("utf-8")
      out += b"Connection: close\r\n"
      body = b""
      #Fill in end
               
      for i in f: #for line in file
      #Fill in start - append your html file contents #Fill in end 
        body += i
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      f.close()
      out += f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")
      connectionSocket.sendall(status + out + body)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      body = b"<html><body><h1>404 Not Found</h1></body></html>"
      out = (b"HTTP/1.1 404 Not Found\r\n"
             + b"Server: Server\r\n"
             + f"Date: {response_date}\r\n".encode("utf-8")
             + b"Content-Type: text/html; charset=UTF-8\r\n"
             + b"Connection: close\r\n"
             + f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")
             + body)
      connectionSocket.sendall(out)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
