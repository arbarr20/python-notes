import time
import threading
from functools import wraps
from queue import Queue
import logging
logging.basicConfig(level=logging.DEBUG, format='%(processName)s PID %(process)d: %(threadName)s:  %(message)s',)
"""
Cada Generador es un Actor
Cada Actor se ejecuta en un Hilo separado
Un actor envia mensajes al otro actor mediante un _registry
el contenido de esteregistro es el actor destino y el mensaje, 
que posterior se guardara en una cola, esta cola esta siendo monitoreada
constantemente por otro hilo (Actor) destino, quien saca el mensaje de la cola 
y lo envia(send) a su respectivo generador y es procesado
"""
class Actor(threading.Thread):
    _registry = { }
    def __init__(self, name, gen):
        super().__init__()
        self.daemon = True
        self.gen = gen
        self.mailbox = Queue()
        Actor._registry[name] = self
        self.start()# al llamar esta linea  se ejecuta el target especificado por run

    def send(self, msg):
        logging.info(f'método send, se le enviará esto: {msg} a  :{self}')
        self.mailbox.put(msg)
        logging.info(f'método send, Se Guardó {msg} en la cola {self.mailbox} para que  {self} lo reciba y lo procese ')
    # es el trabajo que ejecuta el hilo cuando se llame a start
    def run(self):
        while True:
            logging.info(f"método run self:{self}")
            msg = self.mailbox.get()
            logging.info(f"método run, El Hilo {self} obtiene el msg:{msg} de la cola y lo envía al actor {self.gen}")
            self.gen.send(msg)

def send(name, msg):
    logging.info(f'función send, envía al {Actor._registry[name]} llamado {name} el mensaje {msg}')
    #send es el método send de la Clase Actor
    # se cambia de hilo ( de actor)
    Actor._registry[name].send(msg)

def actor(func):
    @wraps(func)# para que no se pierda el diccionario de atributos
    def wrapper(*args, id=func.__name__, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        #convierte a la función decorada en un actor
        return Actor(id, gen)
    return wrapper

@actor
def ping():
    while True:
        n = yield
        logging.info(f'soy el actor ping y recibí el mensaje {n} ahora enviaré a pong el mensaje {n+1}')
        send('pong', n + 1)

@actor
def pong():
    while True:
        n = yield
        logging.info(f'soy el actor pong y recibí el mensaje {n} ahora enviaré a ping el mensaje {n+1} ')
        send('ping', n + 1)

if __name__ == '__main__':
    ping()# actor 1
    pong()# actor 2
    send('ping', 0)
    while True:
        logging.info('main')
        time.sleep(1)


