#!/usr/bin/python
import time #required for sleep
print("hello world")
print("python")
for i in range(1,4): #print beeps at end of program
    print(" %d beeps\a") %i
    time.sleep(1)
