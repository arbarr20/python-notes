import logging
import sys

#creando el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# creando el handler y seteandolo al nivel de debug
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.WARNING)

#creando el formatter
formatter = logging.Formatter('%(asctime)a : %(name)s : %(levelname)s : %(message)s')

#agregando el formato al handler
ch.setFormatter(formatter)

#agregar el handler al logger
logger.addHandler(ch)

#codigo de aplicacion
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
