import logging
import secrets

logger = logging.getLogger(__name__)

def token_gen():
    callerInfo =logger.findCaller(stacklevel=1,stack_info=True)#2
    #callerInfo =str(logger.findCaller(stacklevel=1,stack_info=True)) #1
    print(type(callerInfo))
    logger.debug(f'caller info {callerInfo}')#2
    #logger.debug('caller info %s  ' %(callerInfo))#1

    for i in range(5):
        token = secrets.token_hex(16)
        logger.debug('generated 16 bytes token [%s ]'%token)
