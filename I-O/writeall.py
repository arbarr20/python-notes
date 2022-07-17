text = 'x'*100000000
binary = b'x'*100000000
from timethis import timethis

for n in range(10):
    with timethis("Writing text"):
        open("big.txt","w").write(text)

    with timethis("Writing binary"):
        open("big.txt","wb").write(binary)

import os
os.remove('big.txt')
