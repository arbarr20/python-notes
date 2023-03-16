# Archivo: interfaz_formal_metaclass_abc.py
# Autor: Arbarr20 y ayuda online
# Fecha: 28/02/2023
# Descripción: Interfaz formal con una metaclase abc

'''
El código define una interfaz abstracta FormalParserInterface con dos métodos load_data_source y 
extract_text. Luego se define la clase PdfParserNew que implementa la interfaz
FormalParserInterface y define los métodos necesarios. Se realiza una comprobación de si
PdfParserNew es subclase e instancia de FormalParserInterface.

Luego se define la clase EmlParserNew que también implementa FormalParserInterface, pero define un
método adicional extract_text_from_email que no forma parte de la interfaz. Se realiza una
comprobación de si EmlParserNew es subclase e instancia de FormalParserInterface.
'''

import abc


class FormalParserInterface(metaclass=abc.ABCMeta):
    """
    Clase abstracta que define la interfaz formal que deben seguir
    los parsers de diferentes tipos de documentos.

    Métodos abstractos:
    ------------------
    load_data_source(path: str, file_name: str) -> str:
        Carga los datos de origen del documento.

    extract_text(full_file_path: str) -> dict:
        Extrae el texto del documento y lo devuelve como un diccionario.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Comprueba si la subclase especificada cumple con la interfaz
        formal definida por esta clase.

        Parámetros:
        -----------
        subclass: class
            Clase que se va a comprobar.

        Devuelve:
        --------
        bool:
            True si la clase cumple con la interfaz formal, False en caso contrario.
        """
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class PdfParserNew:
    """
    Parser de archivos PDF que implementa la interfaz formal FormalParserInterface.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """
        Carga los datos de origen del archivo PDF especificado por la ruta
        de acceso y el nombre de archivo proporcionados.

        Parámetros:
        -----------
        path: str
            Ruta de acceso al archivo PDF.

        file_name: str
            Nombre del archivo PDF.

        Devuelve:
        --------
        str:
            Cadena que representa los datos de origen del archivo PDF.
        """
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """
        Extrae el texto del archivo PDF especificado por la ruta de acceso completa
        proporcionada y lo devuelve como un diccionario.

        Parámetros:
        -----------
        full_file_path: str
            Ruta de acceso completa al archivo PDF.

        Devuelve:
        --------
        dict:
            Diccionario que representa el texto extraído del archivo PDF.
        """
        pass


print(f"\n\n--- type de PdfParserNew:{type(PdfParserNew)}")
t = issubclass(PdfParserNew, FormalParserInterface)
print(f"\n**PdfParserNew es subclase de FormalParserInterface?:{t} ")
n = isinstance(PdfParserNew, FormalParserInterface)
print(f"\n**PdfParserNwe es instancia de FormalParserInterface?:{n} ")

instance_PdfParser = PdfParserNew()
ins = isinstance(instance_PdfParser, PdfParserNew)
print(f"\n**instance_PdfParser es instancia de PdfParserNew?:{ins} ")
inst = isinstance(instance_PdfParser, FormalParserInterface)
print(f"\n**instance_PdfParser es instancia de FormalParserInterface?:{inst} ")


class EmlParserNew:
    """
    Parser de correos electrónicos que implementa la interfaz formal FormalParserInterface.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """
        Carga los datos de origen del correo electrónico especificado por la ruta
        de acceso y el nombre de archivo proporcionados.

        Parámetros:
        -----------
        path: str
            Ruta de acceso al correo electrónico.

        file_name: str
            Nombre del correo electrónico.

        Devuelve:
        --------
        str:
            Cadena que representa los datos de origen del correo electrónico.
        """
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """
        Extrae el texto del correo electrónico especificado por la ruta de acceso completa
        proporcionada y lo devuelve como un diccionario.

        Parámetros:
        -----------
        full_file_path: str
            Ruta de acceso completa al correo electrónico.

        Devuelve:
        --------
        dict:
            Diccionario que representa el texto extraído del correo electrónico.
        """
        pass


print(f"\n\n--- type de EmlParserNew:{type(EmlParserNew)}")
l = issubclass(EmlParserNew, FormalParserInterface)
print(f"\n**EmlParserNew es subclase de FormalParserInterface?:{l} ")
j = isinstance(EmlParserNew, FormalParserInterface)
print(f"\n**EmlParserNew es instancia de FormalParserInterface?:{j} ")
instance_EmlParserNew = EmlParserNew()
inst = isinstance(instance_EmlParserNew, EmlParserNew)
print(f"\n**instance_EmlParserNew es instancia de EmlParserNew?:{inst} ")
ins = isinstance(instance_EmlParserNew, FormalParserInterface)
print(
    f"\n**instance_EmlParserNew es instancia de FormalParserInterface?:{ins} "
)
