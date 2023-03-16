import logging
from logging.config import dictConfig
import os
import json

path= 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/logging.json'
if os.path.exists(path):
    with open (path,'rt') as f:
        config =json.load(f)
    dictConfig(config["logging"])

#creando el logger
logger = logging.getLogger('module1')

#codigo de aplicacion
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

