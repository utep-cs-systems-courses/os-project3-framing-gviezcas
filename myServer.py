#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, time
sys.path.append("../lib")       # for params
from lib import params
from archiver import *

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

while True:
    conn, addr = s.accept() # wait until incoming connection request (and accept it)
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        path = "README.md"
        if os.path.exists(path):
            byteArray = writeByteArray(path)
            size = len(byteArray)
            totalsent = 0
            while totalsent < size:
                sent = conn.send(byteArray[totalsent:])
                if sent == 0:
                    raise RuntimeError("Socket connection broken.")
                totalsent += sent
            time.sleep(0.25);       # delay 1/4s
            conn.shutdown(socket.SHUT_WR)
            sys.exit(0)


