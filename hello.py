#!/usr/bin/python3
import time #required for sleep
print("hello world")
print("python")
for i in range(1,4): #print beeps at end of program
    if i ==1:
        print(" %d beep\a" %i)
    else:
        print(" %d beeps\a" %i) 
    time.sleep(1)
