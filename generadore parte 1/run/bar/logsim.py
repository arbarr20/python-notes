import sys
import re

logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
        r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat = re.compile(logpats)



logfilename = "access-lo"
lines   = open(logfilename)
datepat = re.compile(r'\[(\d+)/(\w{3})/(\d+):(\d+):(\d+):(\d+) -(\d+)\]')

lines_m = ((line,datepat.search(line)) for line in lines)

import datetime

months = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5,
        'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10,
        'Nov' : 11, 'Dec' : 12 }

lastdate = None
import time
import sys

f_log = open("run/bar/access-log","w")
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
        
#        print delta.seconds
        time.sleep(delta.seconds/25.0)

    print(line, file=f_log, end='')
    f_log.flush()
    lastdate = date
    
