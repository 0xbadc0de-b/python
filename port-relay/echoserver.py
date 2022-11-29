#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Author: Mikhail Strizhov
# Date: Feb 27, 2016

# bms: python port relay 검색결과로 proxy 코드(relayserver.py)를 테스트하기 위한 echo 서버 코드

import sys
import socket

def usage():
    print("Usage: ./echoserver [relay host] [relay port]")
    sys.exit(1) 

if __name__=='__main__':
    host = ''
    port = ''
    size = 4096

    # Check command line arguments
    total = len(sys.argv)
    if total < 3:
        usage()

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    
    if not (host or port):
        usage()

    # Connect to the relay server
    # bms: relay server가 먼저 실행되어 있어야 함
    #      relay server에 대한 소켓을 생성
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    # Receive a tunnel host & port information
    data = s.recv(size)

    print("[Connct Relay Server] "+data)

    # Now receive any packets from the relay server and send back
    running  = 1
    while running:
        data = s.recv(size)
        print("[Client] "+data)
        if data:
            s.send("[EchoServer] "+data)
        else:
            running = 0

    s.close()
