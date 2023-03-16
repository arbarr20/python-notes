import logging
from logging.handlers   import MemoryHandler

import secrets

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler(filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/FileHnadleErrors.log',mode='a+')
nullHnadler = logging.NullHandler()
monitor = logging.StreamHandler()
#memoryHandlr = MemoryHandler(capacity=15,target=monitor,flushOnClose=False)
memoryHandlr = MemoryHandler(capacity=15,target=nullHnadler,flushOnClose=False)

logger.addHandler(memoryHandlr)
#apenas completa capacity en memoria, los libera, he inicia a guardar de nuvo y asi en un bucle
# es por esto que solo muestra 5 reeistros en el fichero ademas
# de Division by Zero attemped por que lo escribe directamente en el filehandler

for i in range(20):
    token = secrets.token_hex(16)
    logger.debug("generated 16 bytes Token [%s]" %token)

try:
    1/0
except ZeroDivisionError:
    memoryHandlr.setTarget(filehandler)
    logger.error('Division by Zero attemped')
    memoryHandlr.setTarget(nullHnadler)