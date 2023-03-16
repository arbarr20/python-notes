import logging

class MyAppLogAdapter(logging.LoggerAdapter):
    def process(self,msg,kwargs):
        return '%s %s' %(self.extra['clientId'],msg),kwargs

logger= logging.getLogger('appLogginngAdapter')
logger.setLevel(logging.DEBUG)

#handler
sh= logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# formatter
logFormat = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
sh.setFormatter(logFormat)

#agregando el handler al logger
logger.addHandler(sh)

clienInfo ={'clientId': '1cv45rifi35354'}
#class logging.LoggerAdapter(logger, extra)
loggerAdapter = MyAppLogAdapter(logger, extra=clienInfo)

loggerAdapter.debug('Login Attemped')

logger.debug('Normal Log Message')

clienInfo['clientId']= '12dsf89gsajtruRX'
loggerAdapter.debug('logging attemped')
