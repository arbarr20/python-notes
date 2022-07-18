# inline_puzzle.py
#
#Varios intentos de hacer que funcionen las funciones de la biblioteca (rompecabezas)
from concurrent.futures import ThreadPoolExecutor,wait

class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            # este wait sigue siendo indispensable
            wait([fut])
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        try:
            # este resultado nunca llega a do_func para mostrarlo
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

# ------- Example
if __name__ == '__main__':
    import time    
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=2)
    import logging   
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

    def func(x, y):
        logging.info(f"ejecutando func {x} + {y}")
        time.sleep(1)
        return x + y

    def do_func(x, y):
        try:
            logging.info(f"ejecutando do_func {x} + {y}")
            result = yield pool.submit(func, x, y) 
            # es curioso pero con logging no funciona para el example 3,4           
            #logging.info('Got:', result) # esto genera un error ya que a reult no llega nada
            print('El resultado es:',result)
        except Exception as e:
            # es curioso pero con logging no funciona para el example 3,4
            #logging.info('Failed:', repr(e)) 
            print(e)   
    """ def example1():
        '''
        Broken. La declaración 'yield fut' no produce un objeto futuro adecuado
        lo que genera es un Generador, no un Futuro real
        '''
        def after(delay, fut):
            '''
            Ejecutar un futuro después de un retraso de tiempo.
            '''
            logging.info(f"fuuro dentro examplo {fut}")
            yield pool.submit(time.sleep, delay)
            yield fut

        Task(after(10, do_func(2, 3))).step()
    example1() """

    """     def example2():
        '''
        Roto. Se ejecuta, pero el resultado se pierde.
        '''
        def after(delay, fut):
            '''
            Ejecutar un futuro después de un retraso de tiempo.
            '''
            logging.info(f"example2-after fut= {fut} delay {delay}")
            yield pool.submit(time.sleep, delay)
            logging.info(f"example2-after fut= {fut} delay {delay}")
            # el resultado llega aqui pero no se envia a do_func para que se muestre
            for f in fut:
                logging.info(f"f {f} fut {fut}")
                yield f

        Task(after(10, do_func(2, 3))).step()
    example2() """

    """def example3():
        '''
        Funciona, pero la solución no es obvia.
        '''
        def after(delay, fut):
            '''
            Ejecutar un futuro después de un retraso de tiempo..
            En este cado 5 segundos
            '''
            logging.info(f"example3-after fut= {fut} delay {delay}")
            # para que el script corriera se creo en esta parte del codigo
            # la varible result
            result =yield pool.submit(time.sleep, delay)
            try:
                while True:
                    f = fut.send(result)
                    logging.info(f"f {f} fut {result}")
                    result = yield f
            except StopIteration:
                pass

        Task(after(5, do_func(2, 3))).step()
    example3() """

    """ def example4():
        '''
        Funciona, utilizando el rendimiento de. Pero "yield" y "yield from" ambos usados
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield pool.submit(time.sleep, delay)
            yield from fut

        Task(after(5, do_func(2, 3))).step()
    example4() """

    """ def example5():
        '''
        No funciona. No se puede usar "yield from" en todas partes
        '''
        def after(delay, fut):
            '''
            Ejecutar un futuro después de un retraso de tiempo.
            '''
            yield from pool.submit(time.sleep, delay)
            yield from fut

        Task(after(10, do_func(2, 3))).step() """

    
    
    


