import logging

import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
streamHndlr = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHndlr)

logger.warning('[STDOUT]Higt CPU usage.......')
streamHndlr.setStream(sys.stderr)
logger.warning('[STDOERR]Higt CPU usage.......')