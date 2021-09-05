# busproc.py
#
# Procesador de bus. Esto se ejecuta como un subproceso del ejemplo coprocess.py

import sys
from coprocess import recvfrom
from buses import *
#sys.stdin.buffer.raw.read()
#sys.stdin,filter_on_field("route","22",filter_on_field("direction","North Bound",bus_locations()))
fil= sys.stdin.buffer
recvfrom(fil,filter_on_field("route","22",filter_on_field("direction","North Bound",bus_locations())))
