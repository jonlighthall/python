#!/usr/bin/python
import sys

print("demonstration of arbitrary integer precision")
print("with the exponential factorial")
a1=1**0
print ("a1 = 1**0 = %d" % a1)
a2=2**a1
print ("a2 = 2**1 = %d" % a2)
a3 = 3**a2
x = str( a3 )
print ("a3 = 3**2 = %s and has %i digits" % (x,len(x)))
a4=4**a3
y = str( a4 )
print ("a4 = 4**3**2 = 4**%s = %s and has %i digits" % (x,y,len(y)))

print("this may take a while...")
a5=5**a4
#print("a5 = %d" % a5)

sys.set_int_max_str_digits(999999) 
z = str( a5 )
print ("a5 = 5**4**3**2 = 5**%s = %s...%s and has %i digits" % (y,z[:20], z[-20:],len(z)))
