__author__ = 'Trey'


import socket
target_host = "www.google.com"
target_port = 80
  # create a socket object
  # the AF_INET says we're going to use a ipv4 address or hostname
  # SOCK_STREAM says this will be a tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # connect the client
client.connect((target_host,target_port))
     # send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        # receive some data
response = client.recv(4096)
print response