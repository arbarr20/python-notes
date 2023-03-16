# bytesgen.py
#
# Un ejemplo de encadenamiento de diferentes generadores en un proceso
# canalización (pipeline)  

from genfind import *
from genopen import *
from gencat import *
from gengrep import *

pat    = r'ply-.*\.gz'
logdir = 'www'

filenames = gen_find("access-log*",logdir)
logfiles  = gen_open(filenames)
loglines  = gen_cat(logfiles)
patlines  = gen_grep(pat,loglines)
bytecol   = (line.rsplit(None,1)[1] for line in patlines)
bytes_sent= (int(x) for x in bytecol if x != '-')

print("Total", sum(bytes_sent))