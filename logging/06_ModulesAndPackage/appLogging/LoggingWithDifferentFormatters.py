import logging
import sys
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler= logging.StreamHandler(sys.stdout)

#formato usando{
cf = logging.Formatter('{asctime} : {levelname} : {name} : {message}', style='{')
handler.setFormatter(cf)

# agregando el handler al logger
logger.addHandler(handler)

# otro logger diferente
applogger = logging.getLogger('MyappLogger')
applogger.debug('A message Using { fomtter configuration')

#formato usando '$'
df = logging.Formatter('$asctime : $levelname : $name : $message',style='$')
handler.setFormatter(df)
df.converter = time.gmtime

applogger.debug('A message using $ formtter configuration')

