import logging
from appLogging.LoggerFindCaller  import make_call



logging.basicConfig(filename='depuracion/files/big-examples/06_ModulesAndPackage/appLogging/myapp03.log',level=logging.DEBUG)

rootLogger = logging.getLogger('ModuleFindCaller')
rootLogger.debug('logger Starterd')

def find_caller_demo():
    make_call()

find_caller_demo()