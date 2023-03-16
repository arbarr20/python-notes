import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fileHndlr = logging.FileHandler(filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/Filehandler.log',mode= 'a+')
logger.addHandler(fileHndlr)
logger.info('FileHandler started........')