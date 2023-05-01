#!/usr/bin/python
print("demonstration of arbitrary integer precision")
x = str( 3**2 )
print ("3**2 = %s and has %i digits" % (x,len(x)))
y = str( 4**int(x) )
print ("4**3**2 = 4**%s = %s and has %i digits" % (x,y,len(y)))
print("this may take a while...")
z = str( 5**int(y) )
print ("5**4**3**2 = 5**%s = %s...%s and has %i digits" % (y,z[:20], z[-20:],len(z)))
