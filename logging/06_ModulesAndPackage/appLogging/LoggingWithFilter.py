import logging
import sys

from appLogging.packageA1 import ModuleA2
from appLogging.packageB1 import ModuleB2
from packageB import ModuleM1

logger= logging.getLogger()# cuando pongo __name__ no los muestra (por el level)
# si pongo ('appLogging') muestra todo

logger.setLevel(logging.INFO)

#agregar handler
sh = logging.StreamHandler(stream=sys.stdout)
sh.setLevel(logging.INFO)

# agregando un filtro
onlyAppLogging = logging.Filter('appLogging')# solo muestra los mensajes que estan DENTRO de esta jerarquia

sh.addFilter(onlyAppLogging)

# seteando el handler al logger
logger.addHandler(sh)

logger.info('Hierachy 1 is created') # tambien es descartado por el filtro esta al mismo nivel

#invocando funciondes de los otros modulos
ModuleA2.hello_module()
ModuleB2.hello_module()
ModuleM1.hello_module() # este modulo M1 no esta dentro de appLogging por eso no se muestra
# es descartado por el filtro