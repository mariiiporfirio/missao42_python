#!/usr/bin/env python3 

import sys


if len(sys.argv) != 3: 
    print("None") 
else: 
    list = []
    x = int(sys.argv[1])
    y = int(sys.argv[2]) + 1
    v = range(x,y)

    for n in v:
        list.append(n)

    print(list)
     