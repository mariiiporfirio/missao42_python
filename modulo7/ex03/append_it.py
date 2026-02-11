#!/usr/bin/env python3 

import sys

if len(sys.argv) < 2: 
    print("None") 
else: 
    for x in sys.argv[1:]:
        if x.find("ism") == -1:
            print(x + "ism")