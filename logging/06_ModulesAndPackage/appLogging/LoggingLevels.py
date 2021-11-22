import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("info en el mismo nivel que el logger")
logger.error("error por encima del nivel del logger ")
logger.debug("debug por debajo del nivel del logger")