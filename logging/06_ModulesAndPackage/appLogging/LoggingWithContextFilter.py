import logging
import sys
from logging import LogRecord

class CustomFilter(logging.Filter):
    
    def filter(self, record: LogRecord) -> bool:
        print('\n ******** Filter receiver LogRecord: *******\n')
        # muestra todos los atributos del LogRecod mas los arg pasados en en record
        # esto sirve para ver en realidad como se muestran estros atributor y poder 
        # hacer filtros mas personalizados
        for attr in [a for a in dir(record) if not a.startswith('__')]:
            print('%s : %s '%(attr,getattr(record,attr)))
        # si en el record logger.info(hay un string failure) se muestra el record o mensaje
        if 'Failure' in record.msg:
            return True
        return False

logger = logging.getLogger('CustomFilterLogger')
logger.setLevel(logging.DEBUG)

#handler
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

#Filter
cf = CustomFilter()
sh.addFilter(cf)

#Formater
logFormat = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
sh.setFormatter(logFormat)

logger.addHandler(sh)

#logging record
def custom_filter_demo():
    code = 1590 # args de logRecord args : (1590,)
    #atributo de Logrecord: POD : AACXXX, podria usarlo en el logformat como : %(POD)s
    logger.debug('Client connection Failure: %s', code, stack_info=True, extra={'POD': 'AACXXX'})
custom_filter_demo()

# logging exeption

def custom_filter_demo2():
    try:
        1/0
    except ZeroDivisionError:
        # como no tiene Failure en su mensaje, el filtro lo descarta
        logger.warning('Divide by Zero attemped ', exc_info=sys.exc_info(),stack_info=True)

custom_filter_demo2()
