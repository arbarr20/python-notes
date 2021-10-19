# hosts.py
#
# Encuentre direcciones IP de host únicas

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

hosts = set(r['host'] for r in log)
for h in hosts:
    print(h)