# asyncio_patron_colas.py de realpython
#
#varios productores, que no están asociados entre sí, agregan
#  elementos a una cola. Cada productor puede agregar varios elementos
#  a la cola en momentos escalonados, aleatorios y sin previo aviso.
#  Un grupo de consumidores saca artículos de la cola a medida que van
#  apareciendo, con avidez y sin esperar ninguna otra señal.

import asyncio
import itertools as it
import os
import random
import time
"""
1- se crea una cola
2- se crean un numero determinado de tareas consumidores y tareas productoras
3- await asyncio.gather(*producers) inicia la ejecución de las tareas productores
    y por ende las consumidoras de forma cooperativa
4-se crean los productores concurrentemente entre ellos(await async sleep) permite que sean cooperativos
5- se crean los consumidores concurrentemente entre ellos (await async sleep) permite que sean cooperativos
6-  el productor pone un elemento en la cola, simula que lo procesa (await async sleep) y le da paso al 
    consumidor para que consuma y simule que lo procesa (await async sleep), de esta manera consumidor y productor 
    trabajan de forma cooperativa
7- await q.join() espera a que la cola quede limpia
8- se concelan los consumidores, le se avisa que ya no trabajen mas, no esperen mas datos

"""
# cada productor produce un numero aleotorio en hexadecimal longitud 5
async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()

async def randsleep(caller=None) -> None:
    """
    # cada productor despues de ser creado 1 vez y despues de producir duerme un numero 
    #de tiempo aleotorio, igual pasa con los consumidores, al ser creados y despues de consumir
    """
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    # cada productor produce un numero n aleatorio de veces
    print(f'productor:{name} repite {n} veces')
    for _ in it.repeat(None, n): 
        await randsleep(caller=f"Producer {name} {n} veces")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>" f" in {now-t:0.5f} seconds.")
        #indica que se recuperó el elemento y se completó el trabajo, lleva un contador 
        # decreciente de acuerdo a las tareas que están en la cola
        q.task_done()

async def main(nprod: int, ncon: int):    
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]   
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]   
    # espera hasta que se terminen todos los producers
    await asyncio.gather(*producers)
    #join se desbloquea cuando las tareas inconclusas llegan a cero(q.task_done()) lleva el conteo
    #implicitamente espera a los consumidores también
    await q.join() # se bloquea hasta que las tareas terminen, la cola quede limpia
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=1)
    parser.add_argument("-c", "--ncon", type=int, default=1)
    ns = parser.parse_args()
    start = time.perf_counter()
    #ns.__dict__: {'nprod': 5, 'ncon': 10}
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")