lines = open("access-log").readlines()
binlines = open("access-log","rb").readlines()

from timethis import timethis
for n in range(10):
    with timethis("Write using writelines()"):
        open("hugelog.txt","wt").writelines(lines)

    with timethis("Write binary using writelines()"):
        open("hugelog.txt","wb").writelines(binlines)

import os
os.remove("hugelog.txt")

