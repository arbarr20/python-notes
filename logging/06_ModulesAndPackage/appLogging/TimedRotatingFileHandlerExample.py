import logging
from logging.handlers   import TimedRotatingFileHandler 
import time
import secrets


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

timedrotateFH = TimedRotatingFileHandler(filename="depuracion/files/big-examples/06_ModulesAndPackage/appLogging/timeRotatingLogs/Applog",
    when='M',interval=1,backupCount=0)
#El parametro backupCount determina el numero de ficheros que se crea
# si es cero el numero de ficheros son indefinidos

logger.addHandler(timedrotateFH)

while True:
    for i in range(3):
        time.sleep(10)
        token = secrets.token_hex(16)
        logger.debug("generated 16 bytes token [%s]" %token)
