#!/usr/bin/python
print("demonstrantion of arbitray integer precision")
x = str( 5**4 )
print ("5**4 = %s...%s and has %i digits" % (x[:20], x[-20:],len(x)))
y = str( 5**4**3 )
print ("5**4**3 = %s...%s and has %i digits" % (y[:20], y[-20:],len(y)))
print("this may take a while...")
z = str( 5**4**3**2 )
print ("5**4**3**2 = %s...%s and has %i digits" % (z[:20], z[-20:],len(z)))
