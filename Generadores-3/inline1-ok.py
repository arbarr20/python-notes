from perfil import profile1
from concurrent.futures import ThreadPoolExecutor,wait



class Task:
    def __init__(self, gen):        
        self._gen = gen      
    def step(self, value=None):        
        try:
            # la primer vez que se ejecuta es para inicializar el generador        
            fut = self._gen.send(value)    
            # espere a que el futuro termine, o mas bien a que la tarea tenga un resultado      
            # tenga en cuenta que es por que UN futuro esta ejecutando 
            wait([fut])                     
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


    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        logging.info(f'Ejecutando la Tarea {x} + {y}')    
        time.sleep(1)        
        return f'resultado= {x + y}'
        

    def do_func(x, y):
        logging.info("do_func")
        result = yield pool.submit(func, x, y)        
        logging.info(f'got-resultdo_func {result}')     


    # ejecutando de esta forma no hay problemas sin el wait
    #t=Task(do_func(2,3))     
    #t.step() 
    
    def do_many(n):
        while n>0:                                              
            result = yield pool.submit(func,n,n)
            logging.info(f"{result}") 
            n -= 1 
    # al ejecutar de esta forma sin el wait hay problemas
    # no te preocupes por el profile, solo es un decorador para información estadística del script       
    @profile1        
    def start():
        t2 = Task(do_many(2))
        t2.step()
    start()
