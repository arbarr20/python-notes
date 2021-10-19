#logisim.py
# 
# reescribe las lineas de un fichero en otro fichero con un retardo
# este retardo depende una resta entre el campo de fechas de las lineas

import sys
import re

# patron de las lineas del log
logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
        r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat = re.compile(logpats)



logfilename = "access-log"# lea del fichero principal
lines   = open(logfilename)
#patron para encontrar la cadena [24/Feb/2008:00:15:40 -0600] en cada linea
datepat = re.compile(r'\[(\d+)/(\w{3})/(\d+):(\d+):(\d+):(\d+) -(\d+)\]')

lines_m = ((line,datepat.search(line)) for line in lines)

import datetime

months = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5,
        'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10,
        'Nov' : 11, 'Dec' : 12 }

lastdate = None
import time
import sys

f_log = open("run/foo/access-log","w")# escriba en el fichero actual
for line, m in lines_m:     
    day = int(m.group(1))    
    month = months[m.group(2)]
    year = int(m.group(3))
    hour = int(m.group(4))
    minute = int(m.group(5))
    second = int(m.group(6))

    date = datetime.datetime(year,month,day,hour,minute,second)    
    if lastdate:        
        delta = date - lastdate       
        time.sleep(delta.seconds/25.0)
    # el siguiente print es redirige la salida estandar a un fichero,
    #dicho de otra forma escribe line en el fileobject f_log
    print(line)
    print(line, file=f_log, end='')
    #print(line, end='')
    # limpiamos el buffer para escribir en f_log
    f_log.flush()
    lastdate = date
    
