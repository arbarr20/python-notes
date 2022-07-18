# inline2.py
#
# Futuro en linea con manejo de excepciones 

class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        # este try es nuevo con respecto al script anterior (manejo de errores)
        try:
            #send () o throw () dependiendo lo que pase
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        #Detectar excepciones y pasar al siguiente paso según corresponda
        # este try es nuevo con respecto al script anterior (manejo de errores)
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

# Example
if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    import time
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        logging.info(f'Ejecutando la Tarea {x} + {y}')
        time.sleep(1)
        return x + y

    def do_func(x, y):
        logging.info("do_func")
        # este try es nuevo con respecto al script anterior (manejo de errores)
        try:
            result = yield pool.submit(func, x, y)
            logging.info(f' {result}')
        except Exception as e:
            logging.info(f'failed {repr(e)}')
            

    #t = Task(do_func(2,5))
    t = Task(do_func(2,'tres')) # asi se genera un error que es manejado por el programa
    t.step()



    

