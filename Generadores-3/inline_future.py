# inline_future.py
#
# Final implementation
from perfil import profile
from concurrent.futures import Future
import inspect
import logging
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s:  %(process)d: %(processName)s %(message)s',)

def patch_future(cls):
    # para que el futuro sea un iterable
    def __iter__(self):
        
        #si el futuro no ha terminado
        if not self.done():
            
            yield self
        # si ya termino retorne el resultado
        
        return self.result()
    
    cls.__iter__ = __iter__
    
# esto hace que cada futuro sea un iterable

patch_future(Future)

# como se hereda de Future, todas las task son un Futuro
class Task(Future):
    
    def __init__(self, gen):        
        super().__init__() 
        self._gen = gen
        

    def step(self, value=None, exc=None):
        
        try:
            if exc:
                
                fut = self._gen.throw(exc)
                
            else:
                
                fut = self._gen.send(value)
                
                
            fut.add_done_callback(self._wakeup)
            
        except StopIteration as exc:
            # Establecer el resultado de la tarea (valor de retorno del generador)
            
            self.set_result(exc.value)

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
            
        except Exception as exc:
            self.step(None, exc)

def inlined_future(func):
    # si la función no es un futuro (función generadora) se lanza una excepción
    assert inspect.isgeneratorfunction(func)
    return func

def start_inline_future(fut):
    t = Task(fut)
    t.step()
    return t

def run_inline_future(fut):
    t  = start_inline_future(fut)
    return t.result()

# ------- Example
if __name__ == '__main__':
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        time.sleep(5)
        return x + y

    @inlined_future
    def do_func(x, y):
        try:
            result = yield pool.submit(func, x, y)
            return result
        except Exception as e:
            logging.info('Failed:', repr(e))

    @inlined_future
    def after(delay, fut):
        '''
        Run a future after a time delay.
        '''
        yield from pool.submit(time.sleep, delay)
        result = yield from fut
        return result

    # despues de 5 seg ejecute 2 futuros (y son2 futuros= 10seg), el futuro demora 5 seg según la espera de func
    # en total semora 20 segundos
    # SI ejecuta la funcion patch_future
    ''' @profile
    def despues_delay_ejecutefuturo():
        logging.info(f"main")
        result3 = run_inline_future(after(5, do_func(1,1)))
        result4 = run_inline_future(after(5, do_func(2,2)))
        logging.info('Result')
        print('Result:', result3)
        print('Result:', result4)
    despues_delay_ejecutefuturo() '''

        #se demora en ejecutarse 10sg según la espera en func
        # no se ejecuta la funcion patch_future
    #@profile
    def no_concurrente():
        result = run_inline_future(do_func(1,1))
        result2 = run_inline_future(do_func(2,2))
        print('Result:', result)
        print('Result:', result2)
    no_concurrente() 



    # de esta forma se demora 5sg, según la espera en func
    """ @profile
    def concurrente():
        logging.info(f"main")
        t1 = start_inline_future(do_func(1, 1))
        t2 = start_inline_future(do_func(2, 2))
        result1 = t1.result()
        result2 = t2.result()
        logging.info('Result')
        print(result1)
        print(result2)
    concurrente() """