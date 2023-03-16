import logging

PATH = 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/myapp02.log'
logging.basicConfig (filename=PATH,format='%(asctime)s : %(levelname)s : %(levelno)s : %(name)s :  %(machineID)s : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p', filemode='a+',level=logging.INFO)

dictionary = {'machineID': 'AF2342D','requestID':'PAQSDE2329'}

logging.info('Initiating session',extra=dictionary)