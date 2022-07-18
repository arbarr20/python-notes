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
    logging.info(f"cls:{cls}")
    def __iter__(self):
        logging.info(f"patch_future-selfdef __iter__:{self}")
        #si el futuro no ha terminado
        if not self.done():
            logging.info(f"patch_future if")
            yield self
        # si ya termino retorne el resultado
        logging.info(f"patch_future-selfdef self.result:{self.result()}")
        return self.result()
    
    cls.__iter__ = __iter__
    logging.info(f"patch_future cls.__iter__ = __iter__:{cls.__iter__}")
# esto hace que cada futuro sea un iterable
logging.info(f"funcion parch_futre ejecutandose")
patch_future(Future)

# como se hereda de Future, todas las task son un Futuro
class Task(Future):
    logging.info(f"task")
    def __init__(self, gen):        
        super().__init__() 
        logging.info(f"class Task(Future)--self: {self}  gen:{gen}")       
        self._gen = gen
        

    def step(self, value=None, exc=None):
        logging.info(f"step-self {self} value:{value} exc:{exc}")
        try:
            if exc:
                logging.info(f"step-if-exc")
                fut = self._gen.throw(exc)
                logging.info(f"step-if-exc-fut: {fut} exc:{exc}")
            else:
                logging.info(f"step-else sigue fut = self._gen.send(value)")
                fut = self._gen.send(value)
                
                logging.info(f"step-elsefut: {fut} value:{value} despues de fut = self._gen.send(value)")
            logging.info(f"fuera Else fut: {fut} self: {self} vamos al callbak self._wakeup")
            fut.add_done_callback(self._wakeup)
            logging.info(f"Dfut.add_done_callback(self._wakeup) gen:{self._gen} self: {self} fut: {fut}")
        except StopIteration as exc:
            # Establecer el resultado de la tarea (valor de retorno del generador)
            logging.info(f"step stop iteration  self.set_result(exc.value): {exc.value} ")
            self.set_result(exc.value)

    def _wakeup(self, fut):
        try:
            logging.info(f"_wakeup self:{self} fut: {fut}")
            result = fut.result()
            logging.info(f"_wakeup Dresult = fut.result(): {result} ")
            self.step(result, None)
            logging.info(f"_wakeup Dself.step(result, None) result{result} Termino de enviar resultados")
        except Exception as exc:
            logging.info(f"_wakeup Dexcept Exception as exc:{exc}")
            self.step(None, exc)

def inlined_future(func):
    # si la funcion no es un futuro (funcion generadora) se lanza una exepción
    assert inspect.isgeneratorfunction(func)
    logging.info(f"inlined_future func: {func}")
    return func

def start_inline_future(fut):
    logging.info(f"start_inline_future fut: {fut}")
    t = Task(fut)
    logging.info(f"start_inline_future t: {t} sigue t.step()")
    t.step()
    logging.info(f"start_inline_future t despues de step: {t} termino start_inline_future ")
    return t

def run_inline_future(fut):
    logging.info(f"run_inline_future. fut:{fut}")
    t  = start_inline_future(fut)
    logging.info(f"run_inline_future. t:{t}, t.result: {t.result} termino run_inline_future ")
    return t.result()

# ------- Example
if __name__ == '__main__':
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        logging.info(f"func:{x}+{y}")
        time.sleep(5)
        logging.info(f"func:despues del delay de hacer el trabajo ")
        return x + y

    @inlined_future
    def do_func(x, y):
        try:
            logging.info(f"do_func:{x} ,{y}")
            result = yield pool.submit(func, x, y)
            logging.info(f"do_func result:{result}")
            return result
        except Exception as e:
            logging.info('Failed:', repr(e))

    @inlined_future
    def after(delay, fut):
        logging.info(f"def after(delay, fut): {delay} fut: {fut}")
        '''
        Run a future after a time delay.
        '''
        logging.info(f"AFTER yield from pool.submit(time.sleep, delay)")
        yield from pool.submit(time.sleep, delay)
        logging.info(f"Despues de AFTER yield from pool.submit(time.sleep, delay) after:delay:{delay} fut:{fut}")
        result = yield from fut
        logging.info(f"after:result{result}")
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
        logging.info(f"main")
        result = run_inline_future(do_func(1,1))
        result2 = run_inline_future(do_func(2,2))
        logging.info('Result')
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