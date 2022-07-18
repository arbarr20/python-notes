# example of hashing a word list concurrently
from math import ceil
from hashlib import sha512
from os import cpu_count
from concurrent.futures import ProcessPoolExecutor
from perfil import profile1,timethis
import logging
logging.basicConfig(level=logging.DEBUG, format='%(processName)s PID %(process)d: %(threadName)s:  %(message)s',)
CORES= cpu_count()

# hash one word using the SHA algorithm
def hash_word(word):
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data = word.encode('utf-8')    
    # hash the word
    hash_object.update(byte_data)
    # get the hex hash of the word
    has=hash_object.hexdigest()   
    return has

# load a file of words
def load_words(path):
    # open the file
    with open(path) as file:
        # read all data as lines
        lines = file.readlines()  
        return lines



# entry point
@timethis # solo para depuración
def main():
    # load a file of words
    
    path = './generadores3/files/words.txt'    
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    # create the process pool
    with ProcessPoolExecutor(max_workers=CORES) as executor:
        # select a chunk size
        chunksize = ceil(len(words) / CORES)
        print(f"chunksize {chunksize} cpu: {CORES}")
        # create a set of word hashes
        known_words = set(executor.map(hash_word, words, chunksize=chunksize))
    print(f'Done, with {len(known_words)} hashes')

if __name__ == '__main__':
    main()
