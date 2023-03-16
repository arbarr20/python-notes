# inline_recursive.py
#
# Extraño ejemplo recursivo en línea

class Task:
    def __init__(self, gen):
        
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            # para que este script corriera sin problemas fue necesario 
            # introducir wait
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

# Example
if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor,wait
    import time
    import logging   
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

    pool = ThreadPoolExecutor(max_workers=8)

    def recursive(n):
        while n <50:
            yield pool.submit(time.sleep,1)
            #print(('Tick:', n))
            logging.info(f"Tick:, {n}")
            Task(recursive(n+1)).step()
            break

    Task(recursive(0)).step()
