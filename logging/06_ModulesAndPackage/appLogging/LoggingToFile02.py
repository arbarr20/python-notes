import logging

PATH = 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/myapp02.log'
logging.basicConfig (filename=PATH,format='%(asctime)s : %(levelname)s : %(module)s : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p', filemode='a+',level=logging.INFO)
logging.info('logging started ...')