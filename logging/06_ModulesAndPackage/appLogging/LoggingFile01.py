import logging
logging.basicConfig (filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/myapp01.log',filemode='a+',level=logging.INFO)
logging.info('logging started ...')

# usando variables con logging

a = 13
msg = "esto es un valor tipo string"

logging.info("variable a -> %d y string %s " %(a,msg))