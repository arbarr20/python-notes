# simplefuture.py
#
# Ilustración de un futuro

from concurrent.futures import ThreadPoolExecutor

def func(x, y):
    
    import time
    time.sleep(1)
    return x + y

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=8)

    def example1():
        '''
        Bloqueo. Esperar resultados futuros
        '''
        fut = pool.submit(func, 2, 3)
        r = fut.result()
        print('Got:', r)

    def example2():
        '''
        Bloqueo. Con manejo de excepciones.
        '''
        fut = pool.submit(func, 2, 'Hello')
        try:
            r = fut.result()
            print('resultado:', r)
        except Exception as e:
            print('error:', e)

    def example3():
        '''
        Bloqueo...With callback.
        '''
        fut = pool.submit(func, 2, 3)
        fut.add_done_callback(result_handler)

    def result_handler(fut):
        try:
            result = fut.result()
            print('Got:', result)
        except Exception as e:
            print('Whoops:', e)


    example1()
    example2()
    example3()
