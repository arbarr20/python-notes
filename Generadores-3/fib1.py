# fib1.py
#
# Initial fibonacci example using inline futures

#from multiprocessing import freeze_support
import logging
from inline_future import inlined_future, run_inline_future
from concurrent.futures import ProcessPoolExecutor
import time

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result

if __name__ == '__main__':
    
    pool = ProcessPoolExecutor(4)
    start = time.time()
    result = run_inline_future(compute_fibs(34))
    end = time.time()
    print("inline:", end-start)
