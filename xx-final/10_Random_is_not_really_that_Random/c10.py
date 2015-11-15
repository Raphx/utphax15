#!/usr/bin/env python

import socket
import base64
import string

def rot13(s):
    _rot13 = string.maketrans( 
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz ", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm ")
    return string.translate(s, _rot13)

def main():
    soc = socket.socket()
    soc.connect(('mawar.utphax.my', 10081))
    
    count = 1
    while True:
        q = soc.recv(2048)
        qq = q.strip("\n").split("\n\n")
        print qq

        qq = qq[-1]
        if count == 1:
            sol = base64.b64decode(qq)
        elif count == 2:
            sol = rot13(qq)
        elif count == 3:
            sol = unicode(qq, 'cp500', 'ignore').encode('ascii')

        print sol
        soc.send(sol + '\n')
        count += 1

if __name__ == '__main__':
    main()