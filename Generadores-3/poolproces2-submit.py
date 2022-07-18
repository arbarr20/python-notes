# example of hashing a word list concurrently
from math import ceil
from hashlib import sha512
from os import cpu_count
from concurrent.futures import ProcessPoolExecutor,as_completed
from perfil import timethis
import logging
logging.basicConfig(level=logging.DEBUG, format='%(processName)s PID %(process)d: %(threadName)s:  %(message)s',)
CORES= cpu_count()

# hash one word using the SHA algorithm
# para dividir el trabajo con submit esta función tubo varias modificaciones
# mire las listas comprimidas
def hash_word(words):   
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data= [word.encode('utf-8') for word in words]    
    # hash the word
    hash= [hash_object.update(byte) for byte in byte_data]
    # get the hex hash of the word
    hash_hex=[hash_object.hexdigest()for _ in hash]  
    return hash_hex

# load a file of words
def load_words(path):
    # open the file
    with open(path) as file:
        # read all data as lines
        lines = file.readlines()  
        return lines

# entry point
@timethis
def main():
    # load a file of words
    path = './generadores3/files/words.txt'    
    words = load_words(path)
    chunksize = ceil(len(words) / CORES)
    # la siguiente linea es una de las claves para dividir el trabajo con submit
    lista=[words[0:chunksize],words[chunksize:chunksize*2],words[chunksize*2:chunksize*3],words[chunksize*3:chunksize*4],words[chunksize*4:chunksize*5],words[chunksize*5:chunksize*6],words[chunksize*6:chunksize*7],words[chunksize*7:]]
    print(f'Loaded {len(words)} words from {path}')
    # create the process pool
    with ProcessPoolExecutor(max_workers=CORES) as executor:
        t=0
        known_words = set([executor.submit(hash_word, i) for i in lista])
        for future in as_completed(known_words):
            #result = future.result()
            t+=len(future.result())
        
        print(f'Done, with {t} hashes')
        
if __name__ == '__main__':
    main()
