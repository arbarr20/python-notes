import logging
from packageA1.ModuleA4 import token_gen



logger=logging.getLogger(__name__)
def make_call():
    logger.debug('Invoking make_call()')
    token_gen()