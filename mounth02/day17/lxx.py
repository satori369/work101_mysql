from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
