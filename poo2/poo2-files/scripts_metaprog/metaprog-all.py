# Archivo: metaprog-all.py
# Autor: Arbarr20
# Fecha: 29/11/2022
# Descripción: Ciclo de creación de una instancia y de una Clase


class Meta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        com = (mcs, name, bases, kwargs)
        print('\nMeta.__prepare__(mcs=%s, name=%r, bases=%s, **%s)' % com)
        return {}

    def __new__(mcs, name, bases, attrs, **kwargs):
        com = (mcs, name, bases, ', '.join(attrs), kwargs)
        print('\nMeta.__new__(mcs=%s,name=%r,bases=%s,attrs=[%s],**%s)' % com)
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        com = (cls, name, bases, ', '.join(attrs), kwargs)       
        print('\nMeta.__init__(cls=%s,name=%r,bases=%s,attrs=[%s],**%s)' % com)
        return super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        complement = (cls, args, kwargs)
        print('\nMeta.__call__(cls=%s, args=%s, kwargs=%s)' % complement)
        return super().__call__(*args, **kwargs)


class MiClase(metaclass=Meta, extra=1):
    attr = 87884

    def __new__(cls, myarg):
        print('\nMiClase.__new__(cls=%s, myarg=%s)' % (cls, myarg))
        return super().__new__(cls)

    def __init__(self, myarg):
        print('   \nMiClase.__init__(self=%s, myarg=%s)' % (self, myarg))
        self.myarg = myarg
        return super().__init__()

    def __str__(self):
        com = (getattr(self, 'myarg', 'MISSING'),)
        return "<instance of  MiClase; myargs=%s>" % com


obj = MiClase(3)
print(obj)

"""
Salida creación de la Clase
- Meta.__prepare__(mcs=<class '__main__.Meta'>, name='MiClase', bases=(),
  **{'extra': 1})
- Meta.__new__(mcs=<class '__main__.Meta'>, name='MiClase', bases=(),
   attrs=[__module__, __qualname__, attr, __new__, __init__, __str__, 
     __classcell__], **{'extra': 1})
- Meta.__init__(cls=<class '__main__.MiClase'>, name='MiClase', bases=(),
   attrs=[__module__, __qualname__, attr, __new__, __init__, __str__,
      __classcell__], **{'extra': 1})

Creacion de la INSTANCIA
-Meta.__call__(cls=<class '__main__.MiClase'>, args=(3,), kwargs={})
- MiClase.__new__(cls=<class '__main__.MiClase'>, myarg=3)
- MiClase.__init__(self=<instance of  MiClase; myargs=MISSING>, myarg=3)
- <instance of  MiClase; myargs=3>
"""
