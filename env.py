#!/usr/bin/python3
import os
 
# printing environment variables
print(os.environ)
print(os.environ['HOME'])
if 'THISVAR' in os.environ:
    print("this var found")
    print(os.environ['THISVAR'])
else:
    print("this var not found")
