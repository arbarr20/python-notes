# structpack.py
#
# Compare extending a bytearray with packing a bytearray in place

from timethis import timethis
import struct
from random import random

# Create a million random (x,y) points
points = [(random(),random()) for n in range(1000000)]

# Pack a bytearray and write it all at once
with timethis("Packing a bytearray by extending"):
    out = bytearray()
    out.extend(struct.pack("I",len(points)))
    for p in points:
        out.extend(struct.pack("ff",*p))

# Pack a byte array in place
with timethis("Packing a bytearray in place"):
    recordsize = struct.calcsize("ff")
    out = bytearray(4 + len(points)*recordsize)
    struct.pack_into("I",out,0,len(points))
    offset = 4
    for n,p in enumerate(points):
        struct.pack_into("ff",out,4+n*recordsize,*p)

        
    


