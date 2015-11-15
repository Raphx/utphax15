#!/usr/bin/env python

import socket
import re

def main():
    soc = socket.socket()
    soc.connect(('mawar.utphax.my', 20011))

    while True:
        print soc.recv(2048)
        q = soc.recv(2048)
        qq = re.sub(r'What is | \?', "", q)
        ans = str(eval(qq))

        print qq, ans
        soc.send(ans+'\n')

if __name__ == '__main__':
    main()