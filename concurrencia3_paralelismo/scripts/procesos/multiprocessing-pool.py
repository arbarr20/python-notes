
# Archivo: multiprocessing-pool.py
# Autor: Arbarr20 y ayuda online
# Fecha: 18/05/2023
# Descripción: pool de procesos con multiprocessing

"""
NOTA: para folder muy pequeños la función secuencial es mas efectiva, pero si el folder es grade, 
la función paralelo es mucho mas eficiente.

El script es una implementación de un programa para calcular el hash SHA-512 de todos los archivos 
en una carpeta y sus subcarpetas, ya sea secuencialmente o en paralelo utilizando el módulo 
multiprocessing de Python.

La función compute_digest() utiliza la biblioteca hashlib para calcular el hash SHA-512 de un 
archivo dado. La función lee el archivo en bloques de 8192 bytes, actualiza el hash para cada 
bloque leído y devuelve el hash final como resultado.

La función sequential() itera sobre todos los archivos en una carpeta y sus subcarpetas, y para 
cada archivo, calcula su hash SHA-512 secuencialmente utilizando la función compute_digest(). 
Los resultados se almacenan en un diccionario.

La función parallel() utiliza el módulo multiprocessing de Python para calcular el hash SHA-512 de 
cada archivo en paralelo. Utiliza una piscina de procesos para ejecutar varias instancias de la 
función compute_digest() en paralelo. Los resultados se almacenan en un diccionario que se 
devuelve al fina

Algunos métodos:

* hash.update:La función hash.update() toma un objeto de bytes como argumento y agrega el contenido 
de ese objeto al objeto de hash. La función se puede llamar varias veces con diferentes objetos de 
bytes para agregar más datos al objeto de hash.

* hash.digest():en Python devuelve el valor hash como una cadena de bytes. Es decir, la función 
toma el objeto de hash y devuelve un objeto de bytes que representa el valor hash del objeto

* apply_async(): devuelve un objeto AsyncResult que se puede utilizar para esperar a que se 
complete la tarea en segundo plano y obtener el resultado. Esto se hace mediante la función 
AsyncResult.get(), que devolverá el resultado de la función func.
En resumen, apply_async() es una función útil de multiprocessing para ejecutar tareas en paralelo 
en varios procesos y recuperar los resultados cuando se completan.

para este script en con
"""

import multiprocessing
import os
import hashlib
import logging
import time
from multiprocessing import freeze_support
import re


logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s:%(process)d] %(message)s')


TOPDIR: str = "/pon/tu/ruta/aquí"


def compute_digest(filename: str) -> bytes:
    """Calcula el hash SHA-512 de un archivo.

    Args:
        filename (str): Nombre del archivo para calcular el hash.

    Returns:
        bytes: El valor de hash SHA-512 del archivo.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe.
    """
    digest = hashlib.sha512()
    f = open(filename, 'rb')
    while True:
        chunk = f.read(8192)
        if not chunk:
            break
        digest.update(chunk)
        nombre_archivo = re.search(r'/([^/]+)$', filename).group(1)
        logging.info(f"""El fichero: {nombre_archivo} tiene el hash: {digest.hexdigest()}\n""")
    f.close()
    return digest.digest()


def sequential() -> dict:
    """Calcula los hashes SHA-512 de los archivos en TOPDIR en secuencia.

    Returns:
        dict: Un diccionario que mapea nombres de archivo a valores de hash SHA-512.
    """
    start = time.time()
    digest_map = {}
    for path, dirs, files in os.walk(TOPDIR):
        for name in files:
            fullname = os.path.join(path, name)
            if os.path.exists(fullname):
                digest_map[fullname] = compute_digest(fullname)
    end = time.time()
    logging.info(f"secuencial: {end-start} seconds")

    return digest_map


def parallel() -> dict:
    """Calcula los hashes SHA-512 de los archivos en TOPDIR en paralelo.

    Returns:
        dict: Un diccionario que mapea nombres de archivo a valores de hash SHA-512.
    """
    start = time.time()
    p = multiprocessing.Pool(2)
    digest_map = {}
    for path, dirs, files in os.walk(TOPDIR):
        for name in files:
            fullname = os.path.join(path, name)
            if os.path.exists(fullname):
                digest_map[fullname] = p.apply_async(compute_digest, (fullname,))

    for filename, result in digest_map.items():
        digest_map[filename] = result.get()
    end = time.time()
    logging.info(f"paralelo:{end-start} seconds")
    return digest_map


if __name__ == '__main__':
    freeze_support()
    map1 = sequential()
    map2 = parallel()
    assert map1 == map2
