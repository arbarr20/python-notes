import logging

from project import add_module_handler

logger = logging.getLogger(__name__)
add_module_handler(logger)

def func2():
    logger.debug("debug called from utils.func2()")
    logger.critical("critical called from utils.func2()")