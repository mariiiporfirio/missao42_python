#!/usr/bin/env python3 
import sys, re 

if len(sys.argv) != 2: 
    print("None") 
else: 
    finder = re.findall(r"z",sys.argv[1]) 
    if len(finder) > 0: 
        print("".join(finder)) 
    elif len(finder) == 0: 
        print("None") 
