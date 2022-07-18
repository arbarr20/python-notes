#Chaining_Coroutines
# tomado de realpython.com

import asyncio
import random
import time
#part1 duerme durante un tiempo variable y part 2 inicia a trabajar con los resultados que van llegando
async def part1(n: int) -> str:
    # numero aleatorio de 0 a 10 con la semilla (444)
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    # numero aleatorio de 0 a 10 con la semilla (444)
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    # p1 ejecuta los 3 parametros que contiene n, uno tras otro
    p1 = await part1(n)
    # a medida que p1 entrega resultados (se cumplen los tiempos según sus parametros)
    #p2 inicia a trabajar con estos resultasos
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    # semilla para numeros aleatorios
    random.seed(444)
    # si no hay argumentos a la hora de ejecutar el script ejemplo: python3 chained.py "no args"
    # por defecto asigna [1,2,3] de lo contrario guarda los introducidos en los argumentos.
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    #contador preciso
    start = time.perf_counter()
    #*args: recibe multiples argumentos
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")