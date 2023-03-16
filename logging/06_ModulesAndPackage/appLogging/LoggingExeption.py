import logging

logging.basicConfig(filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/MyaplicationExeption.log')

try:
    1/0
except ZeroDivisionError:
    logging.exception("Division by Zero is performed")