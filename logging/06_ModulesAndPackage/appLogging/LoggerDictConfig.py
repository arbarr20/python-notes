import logging
from logging.config import dictConfig
import os
import yaml

path= 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/logging.yml'
if os.path.exists(path):
    with open (path,'rt') as f:
        config =yaml.safe_load(f.read())
    dictConfig(config)

#creando el logger
logger = logging.getLogger('module1')

#codigo de aplicacion
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')



