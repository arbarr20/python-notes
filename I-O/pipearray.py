# pipearray.py
#
# Create a large array in a parent process and send it to a child process
# using a pipe

import subprocess
import array

# 10 million item array
a = array.array("I",range(10000000))

# Launch a subprocess and write the array
p = subprocess.Popen(['python3','getarray.py'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE,
                     bufsize=65536)

# Write directly onto the pipe. Notice how there is no need
# to convert a into a string (underlying memory used directly)
p.stdin.write(a)
print(p.stdout.read().decode())
