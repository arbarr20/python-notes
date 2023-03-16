import logging
from logging.handlers import RotatingFileHandler

import secrets

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotatingFH = RotatingFileHandler(filename="depuracion/files/big-examples/06_ModulesAndPackage/appLogging/rotaringLogs/Applog",
mode='a+',maxBytes=500, backupCount=5)
rotatingFH.setFormatter(formatter)
#maximo creara 5 ficheros de 500Bytes cada uno, 
#lo que se pase de eso se eliminaran los viejos y se guardaran los nuevos
logger.addHandler(rotatingFH)




for i in range(500):
    token = secrets.token_hex(16)
    logger.debug("generated 16 bytes token [%s]" %token)
