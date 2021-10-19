# query404.py
#
# Encuentre el conjunto de todos los documentos que 404 en un archivo de registro

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("log","www")
log = apache_log(lines)

stat404 =  {  r['request'] for r in log if r['status'] == 404 }

for r in sorted(stat404):
    
    print(r)