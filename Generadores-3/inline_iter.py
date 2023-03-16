# inline_iter.py
#
# Patched Future class to make it suitable for use with yield from by
# making it iterable

from concurrent.futures import Future,wait
import logging   
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

def patch_future(cls):
    logging.info(f"cls:{cls}")
    def __iter__(self):
        logging.info(f"self:{self}")
        #si el futuro no ha terminado
        if not self.done():
            yield self
        # si ya termino retorne el resultado
        logging.info(f"self.result:{self.result()}")
        return self.result()
    cls.__iter__ = __iter__

patch_future(Future)

class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            wait([fut])
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

# ------- Example
if __name__ == '__main__':
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)
    

    def func(x, y):
        logging.info(f"Ejecutando func {x}+{y}")
        time.sleep(1)
        return x + y

    def do_func(x, y):
        try:
            logging.info(f"Ejecutando dp_func {x}+{y}")
            result = yield pool.submit(func, x, y)
            print('Resultado:', result)
        except Exception as e:
            print('Failed:', repr(e))

    def example5():
        '''
        Now it works!
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield from pool.submit(time.sleep, delay)
            logging.info(f"delay:{delay} fut:{fut}")
            yield from fut
            
        Task(after(2, do_func(2, 3))).step()
    example5()

