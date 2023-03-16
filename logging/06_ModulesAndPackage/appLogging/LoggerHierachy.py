import logging

PATH = 'depuracion/files/big-examples/06_ModulesAndPackage/appLogging/MyApplicationHierachy.log'
logging.basicConfig (filename=PATH,format='%(asctime)s : %(levelname)s : %(module)s : %(name)s :  %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p', filemode='a+',level=logging.INFO)

logger = logging.getLogger()
logger.info('Hierachy 1 es created')

from packageA1 import ModuleA2
from packageB1 import ModuleB2

ModuleA2.hello_module()
ModuleB2.hello_module()
