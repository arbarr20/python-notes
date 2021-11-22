import logging
# level logger warning
logger = logging.getLogger(__name__)

def hello_module():
    logger.info('Message from packageB1 -> ModuleB2')

