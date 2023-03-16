import logging
import threading
import random
import time
import secrets

def token_gen (nbytes, ntoken):
    for i in range(ntoken):
        time.sleep(random.uniform(1.0,2.0))
        token = secrets.token_hex(nbytes)
        logging.info('%d Bytes token generated [%s]' %(nbytes,token))

PATH = 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/myapp03.log'
logging.basicConfig (filename=PATH,format='%(asctime)s : %(threadName)s :  %(levelname)s : %(module)s : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p', filemode='a+',level=logging.INFO)

threads = []
for i in range (1,5):
    thread = threading.Thread(target=token_gen, args=(16,3))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('Existing main Program')