import logging
from logging.config import fileConfig

fileConfig('depuracion/files/big-examples/06_ModulesAndPackage/appLogging/logging.conf')

#creando el logger
logger= logging.getLogger('module1')

# codigo de aplicacion
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
