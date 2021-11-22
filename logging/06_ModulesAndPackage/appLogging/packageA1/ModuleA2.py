import logging
# level logger warning
logger = logging.getLogger(__name__)

def hello_module():
    logger.info('Message from packageA1 -> ModuleA2')
    logger.error('Message Error from packageA1 -> ModuleA2')
    