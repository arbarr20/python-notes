import logging

old_factory = logging.getLogRecordFactory()
def record_factory(*arg, **kwargs):
    record = old_factory(*arg,**kwargs)
    record.pod = 'POD_ANXZ1'
    return record

logging.basicConfig(format= '%(asctime)s : %(pod)s : %(levelname)s : %(module)s : %(message)s',datefmt = '%d/%m/%Y %I:%M:%S %p',filemode='a+', level= logging.INFO)

logging.setLogRecordFactory(record_factory)

logging.warning('High CPU usage...')