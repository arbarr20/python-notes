import logging

from logging.handlers   import WatchedFileHandler

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',level=logging.DEBUG,filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/WatchedFilehandler.log',filemode='a+',datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()
log_handler = WatchedFileHandler('depuracion/files/big-examples/06_ModulesAndPackage/appLogging/WatchedFilehandler.log', mode='a+')
#log_handler.setFormatter(logging.Formatter('%(levelname)s:%(asctime)s:%(message)s'))
logger.addHandler(log_handler)

logger.critical("esto es cirtico")
logger.debug("esto es un debug")