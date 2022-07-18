# fib3.py
#
# #Diferente modelo de ejecución de Hilos. Aquí, el futuro en línea está restringido a uno solo.
# hilo de ejecución. Obtiene el mismo rendimiento, pero el flujo de control no cambia los hilos.
"""
en la ejecución paralela de este ejemplo lo entiendo de la siguiente manera:
hay 2 Hilos que se ejecutan de forma concurrente, cada hilo tiene la tarea de 
calcula el numero fibonacci hasta el 34, ahora cada hilo crea 2 procesos.

Hilo1= fib(34)--> 2 procesos
                    1 proceso--fib(1)--espera resultado de futuro
                    2 proceso--fib(2)--espera resultado de futuro
                    1 proceso--fib(3)--espera resultado de futuro
                    2 proceso--fib(4)--espera resultado de futuro
Hilo2= fib(34)--> 2 procesos
                    1 proceso--fib(1)--espera resultado de futuro
                    2 proceso--fib(2)--espera resultado de futuro
                    1 proceso--fib(3)--espera resultado de futuro
                    2 proceso--fib(4)--espera resultado de futuro

"""
from inline_future import inlined_future, run_inline_future
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(processName)s PID %(process)d: %(threadName)s:  %(message)s',)
from functools import lru_cache
def run_inline_thread(gen):
    value = None
    exc = None
    while True:
        #logging.info('run_inline')
        try:
            if exc:
                fut = gen.throw(exc)
            else:
                fut = gen.send(value)
            try:
                value = fut.result()
                exc = None
            except Exception as e:
                exc = e
        except StopIteration as exc:
            return exc.value
#@lru_cache
def fib(n):
    #logging.info('fib')
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        
        #logging.info(f'compute_fib {threading.current_thread()}')    
        val = yield from pool.submit(fib, i)# pone trabajos a los subprocesos
        result.append(val)
        #logging.info(f'compute_fib {result}')
    return result
if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)

    ''' start = time.time()
    result = run_inline_future(compute_fibs(34))
    result = run_inline_future(compute_fibs(34))
    end = time.time()
    logging.info(f"Secuential:{end-start}" ) '''

    tpool = ThreadPoolExecutor(2)
    start = time.time()
    # un hilo esta tirando 2 procesos eso es lo que logro entender es 
    # esta parte del código
    t1 = tpool.submit(run_inline_thread, compute_fibs(34))
    #t2 = tpool.submit(run_inline_thread, compute_fibs(34))
    result1 = t1.result()
    #result2 = t2.result()
    end = time.time()
    logging.info(f"Parallel:{end-start}, Resultado={result1}" )




