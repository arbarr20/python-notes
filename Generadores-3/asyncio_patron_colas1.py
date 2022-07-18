# asyncio 
# Distribuir las cargas de trabajo entre varios tareas concurrentementes



import asyncio
import random
import time

"""
1- se crea una cola
2- de forma bloqueante (hasta que no se ingresan los 20 no se saca nada de la cola) se ingresan 
    a la cola 20 elementos (generadores de datos)
3- se crean 3 tareas (workers), y await queue.join() (esto envía a ejecutar las tareas y hasta que no terminen no regrese ) 
    las tareas sacan datos de la cola de fora cooperativa,
    procesan estos datos (await async sleep()),mientra están procesando estos datos ceden el control para
    que otra worker ejecute otra tarea (sacar de la cola y procesar
4- A medida que se terminan se procesar los datos, las tareas se terminan ( queue.task_done())
5- se deben candelar cada tarea con task.cancel()
6- parece redundante pero await asyncio.gather(*tasks, return_exceptions=True) se cerciora que todas las tareas
    terminen sus tareas
"""


async def worker(name, queue):
    while True:
        # Saca un "elemento de trabajo" de la cola.
        sleep_for = await queue.get()
        print(f"tarea {name} trabajando por {sleep_for:.2f} segundos")

        # Dormir durante los segundos "sleep_for"
        await asyncio.sleep(sleep_for)

        #Notifique a la cola que se ha procesado el "elemento de trabajo".
        
        queue.task_done()

        print(f'tarea {name} terminada,ha dormido por {sleep_for:.2f} seconds')


async def main():
    # Cree una cola que usaremos para almacenar nuestra "carga de trabajo".
    queue = asyncio.Queue()

    # Genere tiempos aleatorios y colóquelos en la cola.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        #Ponga un elemento en la cola sin bloquear.
        queue.put_nowait(sleep_for)

    # Cree tres tareas de trabajo para procesar la cola concurrentemente.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Espere hasta que la cola se procese por completo.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    #Cancelar las tareas de nuestros trabajadores.
    for task in tasks:
        task.cancel()
    # Espere hasta que se cancelen todas las tareas de los trabajadores.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 Los trabajadores durmieron en paralelo durante {total_slept_for:.2f} seconds')
    print(f'tiempo total de retardo esperado: {total_sleep_time:.2f} seconds')


asyncio.run(main())