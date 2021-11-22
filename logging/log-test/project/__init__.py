import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# para cada nivel se crea un fichero con su nombre en muniscula. debug.log
levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
for level in levels:
    handler = logging.FileHandler(f"depuracion/files/log-test/level-{level.lower()}.log")
    handler.setLevel(getattr(logging, level))
    logger.addHandler(handler)

def add_module_handler(logger, level=logging.DEBUG):
    handler = logging.FileHandler(
        f"depuracion/files/log-test/level-{logger.name.replace('.', '-')}.log" )
    handler.setLevel(level)
    logger.addHandler(handler)