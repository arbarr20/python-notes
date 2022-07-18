# inline1.py
#
# Formulación de futuro en línea simple

class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None):
        try:
            # la primer vez que se ejecuta es para inicializar el generador
            fut = self._gen.send(value) 
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        result = fut.result()
        self.step(result)

# Example
if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    import time
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)


    pool = ThreadPoolExecutor(max_workers=2)

    def func(x, y):
        time.sleep(1)
        return x + y

    def do_func(x, y):
        result = yield pool.submit(func, x, y)        
        logging.info(f'got {result}')

    t = Task(do_func(2,3))
    t.step()#debe iniciar el primer paso de la tarea para que se ejecute
    logging.info(f'Haciendo esto mientras termina')
    

    """ # Ejemplo de una función que realiza solicitudes repetidas al pool (no corre bien)
    # pero me genera un error
    def do_many(n):
        while n > 0:
            result = yield pool.submit(func, n, n)
            print('Got:', result)
            n -= 1

    t2 = Task(do_many(10))
    t2.step() """


