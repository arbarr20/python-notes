# realtime404.py
#
# Imprima todas las solicitudes 404 a medida que ocurren en el registro

from apachelog import apache_log
from follow import follow

logfile  = open("run/foo/access-log")
loglines = follow(logfile)
log      = apache_log(loglines)

r404 = (r for r in log if r['status'] == 404)

for r in r404:
    print(r['host'], r['datetime'], r['request'])