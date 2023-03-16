import logging

logging.warning(" Esto es una advertencia")
logging.debug("esto no se imprime en la consolo por que el nivel del loggin es warning ")
logging.error("ocurrio un error")

# configuracion basica
# si no se especifica in filename, la configuracion basica se redirecciona al 'sys.stderr
from appLogging import LoggingDefault

#guardar el logging en in fichero
# se debe declarar una variable file
from appLogging import LoggingFile01

# logging personalizado
from appLogging import LoggingToFile02

# logging con threads (mostrar el nombre de los threads)
from appLogging import LoggingTreads

# parametro extra de logging
# extrta es un diccionario, cuando es usaso setea el record factory
# es un atributo personalizado
# cuidado si no se pone la clave en el diccionario pero esta en el formater
# se leventa una exepcion

from appLogging import LoggingWithExtraParam

#compenentes principales de logging
#loggers
#Handlers
#Filter
#Formatter

# los eventos del log son pasados en una instancia de LogRecord
#depuracion/files/compenenteslogging.png

#funciones del modulo logger

#getLogger()


#class LogRecord
# ver parametro en la wiki
#getMessage()
# la informacion primaria pasda a LogRecord son msg (mensaje que escribo) y args
#getLogRecordFactory(): es usado para crear un LogRecord


#setLogRecodFactory(factory): configuracion para crear un LogRecordFactory
#factory: es usado para instanciar a el registro(record) del log (evento)
#factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)

# estos valores personalizados seran inyectados en el momento de la creación de la siguiente manera: 
# no hay restricciones para crear atributos, pero el nombre de cada atributo debe ser unico
from appLogging import CustomLogRecordFactory

#disable(lever = CRITICAL) el valor por defecto es critico, tenga en cuenta 
# la gerarquia, tambien desabilita

#getLevelName(level): retorna el valor nuerico del log
import logging

print("getLevelName('Info') :",logging.getLevelName('INFO'))
print("getLevelName(40) :",logging.getLevelName(40))

#logging.shutdown( ) 
#Informa al sistema de registro para realizar un apagado ordenado descargando y cerrando todos los manipuladores.
#Esto se debe llamar al salir de la aplicación y no se debe hacer ningún uso posterior del sistema de registro después de esta llamada.

#getLoggerClass(): 
#setLoggerClass(klass):Le dice al sistema de registro que use la clase klass al crear una instancia de un registrador

class Mylogger(logging.getLoggerClass()):
    pass

#logging.makeLogRecord(attrdict):Crea y devuelve una nueva LogRecordinstancia cuyos atributos están definidos por attrdict
#class logger

#Repase la jerarquia del logger

#atrubutos

#level: retorna el nivel del logger
import logging

rootLogger = logging.getLogger()
nonRootLogger = logging.getLogger(__name__)

print('Root logger level:',rootLogger.level)
print('Non-Root Logger level: ',nonRootLogger.level)

#propagate:Si este atributo se evalúa como verdadero, los eventos registrados 
# en este registrador se pasarán a los controladores de los registradores de nivel superior (ancestros)

import logging
logger = logging.getLogger()

print('propagate: ',logger.propagate)

# esto significa que los hijos pueden pasar el mensaje a los handlres de sus padres
# es este ejemplo se puede ver la aplicaion de propagate
#
# esto daba un error no encontraba un paquete, pero se soluciono agregando
#export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
from appLogging import LoggerHierachy 

# funciones

#getEfectiveLevel(): 

import logging

rootLogger = logging.getLogger()
nonRootLogger = logging.getLogger(__name__)

print('Root Logger level:', rootLogger.level)
print('Root Logger EfectiveLevel:',rootLogger.getEffectiveLevel())
print('Non-Root Logger level:',nonRootLogger.level)
print('Non-Root Logger Effective Level:',nonRootLogger.getEffectiveLevel())

# metodos logger

#logging.debug()
#logging.info()...etc

#exeption(msg,*args,**kwargs)

from appLogging import LoggingExeption

#log(level,msg,*args,**kwargs)

import logging

logging.log(logging.WARNING,"warning message from log() method")

#setlevel

from appLogging import LoggingLevels

#addHandler(hdlr):se agrega objeto handler al logger
#removeHandler()
#addFilter()
#removeFilter()

#isEnableFor(level)
#getChield(suffix)

logging.getLogger('packageA').getChild('ModuleA1')
#es lo mismo que
logging.getLogger('packageA.ModuleA1')# para no tener que poner tda la jerarquia se utiliza
#getChild

#handler(record ):
#hasHandlers( ):Comprueba si este registrador tiene algún controlador configurado
#logger.debug(f'caller info {logger.findCaller(stacklevel=1,stack_info=True)}')
#stacklevel = 1: Ruta completa delPRIMER scrpt que llamo a este evento,la linea de donde fue llamado,
# funcion dentro de la primer ruta que realmente ejecuto la llamada a este evento--- esto nos da a conocer que hubo un
#anidamiento entre paquetes y modulos, observe qeu retorna una cierta tupla unos valores separados por comas
#stack_info=True: es parecido al stacklevel, es mas preciso y completo.la informacion de la pila de como se ejeuto el
#llamado a este evento. seria bueno formatearlo para entregar la info bonita
# en resumen findCaller retorna tupla (filename,line number,function name,stack informaion)
# observe log Myapp03  de la siguiente importacion y analicelo .

from appLogging import ModuleFindCaller

#handlers: son los que me dicen a que parte sera enviado el evento, a la consola, a un fichero
#correo electronico, etc, un logger puede tener multiples handlers usando el metodo addhandler()

#Handler class

#costructor handler(level=NONSET)

from logging import FileHandler, Handler,DEBUG

mi_handler = Handler(DEBUG)
print(mi_handler)

# los handler tienen level propios
# se le pueden agregar filtros
#pueden crear un lock para serializar datos de E/S
# no se puede crar directamente (solo herencia)

# tiene una gran catidad de metodos ver la wiki

# subclases implementasos por la biblioteca

#StreamHandler

#constructor
#StreamHandler(stream=None)

#metodos

#emit(record): aemite el record(el log como tal) al steam (a la salida definida) si hay una exepcion, esta
#se presentara usando el formato traceback.

# flush(): bacia el buffer del stream  (para que se muestre el mensaje)
#setStream(stream): MemoryHandler

#Atributos:
# terminator:Cadena utilizada como terminador al escribir un registro formateado en una secuencia. El valor predeterminado es '\n'.

from appLogging import StreamHandlerExample

#File Handlers

from appLogging import FileHandlerExample

#RotatingFileHandler

from appLogging import RotatingFileHandlerExample

#TimedRotatingFileHandler

from appLogging import TimedRotatingFileHandlerExample

#SMTPHandler
# este ejemplo lo encontre en la web y  se modifico
#para enviar el correo a gmail.
from appLogging import SMTPHandlerExample

#MemoryHandler
from appLogging import MemoryHandlerExample

# WatchedFileHandler no hay ejemplo y tampoco en la web
# no lo entiendo muy bien pero se debe tener en cuanta cuando se usa
# syslog

from appLogging import WatchedFileHandlerExample

#QueueHandler

from appLogging import LoggingWithQueueHandler

#Filter

from appLogging import LoggingWithFilter

# Filter contextual Information
"""
contextual informaition

def filter(record:LogRecord)->int:
    pass
record puede acceder a los tributos LogRecord por medios
de los *ags. y modificarlos en la funcion filter y asi
agregar informacion contextual
"""
from appLogging import LoggingWithContextFilter

# no es necesario crear una clase para crear un filtro como en el ejemplo anterior,
#aqui otro ejemplo solo sobreescribiendo la funcion fulter
from appLogging import LoggingWithContextFilter2

#LoggerAdapter  -- es mejor que el filter este aplica a toda la gerarquia del logger

from appLogging import LoggerAdapterExample

#formatter
from appLogging import LoggingWithDifferentFormatters

# confiuracion de loggng
# configuracion basica del propio modulo

from appLogging import LoggerComponents

# configuracion por medio de fichero de configuracion .conf
# se crea un fichero logging.cong y luego se llama desde LoggerFileConfig
from appLogging import LoggerFileConfig

# configuracion por medio de diccionario de configuracion desde in fichero YAML
# se crea un fichero logging.yml y luego se llama desde LoggerDictConfig
# me parece mas facil de usar este.
from appLogging import LoggerDictConfig

# configuracion por medio de diccionario de configuracion desde in fichero JSON
# se crea un fichero logging.json y luego se llama desde LoggerDictConfig2
from appLogging import LoggerDictConfig2