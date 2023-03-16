# actor3.py
#
# Stackless recursive ping-pong

from collections import deque
import logging
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

_registry = { }
_msg_queue = deque()

def send(name, msg):
    _msg_queue.append((name, msg))

def run():
    while _msg_queue:
        name, msg = _msg_queue.popleft()
        #envie al generador lo que se saca de la cola de mensajes
        _registry[name].send(msg)

def actor(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        _registry[func.__name__] = gen
    return wrapper

@actor
def ping():
    while True:
        n = yield
        #print('ping %d' % n)
        logging.info('ping %d' % n)
        send('pong', n + 1)

@actor
def pong():
    while True:
        n = yield
        #print('pong %d' % n)
        logging.info('pong %d' % n)
        send('ping', n + 1)

ping()
pong()
send('ping', 0)
# run es la clave, es el bucle que siempre se
#esta ejecutando
run()
