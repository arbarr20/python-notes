from logging.handlers import QueueHandler,QueueListener
import queue
import logging
import sys

logQueue = queue.SimpleQueue()
qhandler = QueueHandler(logQueue)

handler = logging.StreamHandler(sys.stdout) # este handler puede ser reemplazado por un SMTP handler
listener = QueueListener(logQueue,handler)

logger= logging.getLogger()
logger.addHandler(qhandler)

listener.start()

logging.warning('========    A message through queue     =========')
logging.warning('+++++++++    Second message through queue   +++++++++')

listener.stop() # si no lo llamas antes de que la app termine, puede  que algunosmensajes no se muestren