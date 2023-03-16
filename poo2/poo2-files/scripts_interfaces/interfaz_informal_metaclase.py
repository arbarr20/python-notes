# Archivo: interfaz_informal_metaclase.py
# Autor: Arbarr20 y ayuda online
# Fecha: 24/02/2023
# Descripción: definición de una interfaz informal con metaclase

'''
"""
El script define una metaclase llamada ParserMeta que se utiliza para crear clases de 
Interfaz_Analizador(parser) y garantizar que las subclases implementen los métodos load_data_source
y extract_text.
Luego, define una clase abstracta UpdatedInformalParserInterface que hereda de la metaclase
ParserMeta. Esta clase abstracta sirve como interfaz para heredar clases concretas, pero no es
necesario definir los métodos de ParserMeta ya que están implícitamente disponibles a través de 
__subclasscheck__ ().

El script también define dos implementaciones concretas PdfParserNew y EmlParserNew. La clase 
PdfParserNew implementa los métodos load_data_source y extract_text tal como se especifica en la 
interfaz, por lo que se considera una subclase de UpdatedInformalParserInterface. La clase
EmlParserNew implementa el método load_data_source tal como se especifica en la interfaz, pero no 
implementa el método extract_text y en su lugar tiene un método llamado extract_text_from_email.
Por lo tanto, no se considera una subclase de UpdatedInformalParserInterface.
'''


class ParserMeta(type):
    """Una metaclase de analizador(parser) que se utilizará
    para la creación de clases de analizador(parser).

    Métodos:
    __instancecheck__(cls, instance) -- revisa si una instancia es una subclase de la clase
    __subclasscheck__(cls, subclass) -- revisa si una subclase implementa los métodos necesarios
    para ser una subclase de UpdatedInformalParserInterface
    """

    def __instancecheck__(cls, instance):
        """
        Revisa si una instancia es una subclase de la clase.
        :param cls: Clase actual.
        :type cls: type
        :param instance: Instancia de una clase.
        :type instance: object
        :return: True si es subclase, de lo contrario False.
        :rtype: bool
        """
        print(f"instance clc: {cls}-instance {type(instance)}")
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        """
        Revisa si una subclase implementa los métodos necesarios para ser una subclase de 
        UpdatedInformalParserInterface.
        :param cls: Clase actual.
        :type cls: type
        :param subclass: Subclase de una clase.
        :type subclass: type
        :return: True si implementa los métodos, de lo contrario False.
        :rtype: bool
        """
        print(f"clc: {cls}-subclass {subclass}")
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
        )


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """
    Su interfaz se utiliza para heredar clases concretas.
    No es necesario definir los métodos ParserMeta como cualquier
    clase ya que están implícitamente disponibles a través de .__subclasscheck__().

    Métodos:
    No tiene métodos.
    """

    pass


print(
    f"\n\n--- type de UpdatedInformalParserInterface:{type(UpdatedInformalParserInterface)}"
)
t = issubclass(UpdatedInformalParserInterface, ParserMeta)
print(f"\n**UpdatedInformalParserInterface es subclase de ParserMeta?:{t} ")
n = isinstance(UpdatedInformalParserInterface, ParserMeta)
print(f"\n**UpdatedInformalParserInterface es instancia de ParserMeta?:{n} ")

instance_UpdatedInformalParserInterface = UpdatedInformalParserInterface()
ins = isinstance(
    instance_UpdatedInformalParserInterface, UpdatedInformalParserInterface
)
print(
    f"\n**instance_UpdatedInformalParserInterface es instancia de UpdatedInformalParserInterface?:\
        {ins} "
)
ins = isinstance(instance_UpdatedInformalParserInterface, ParserMeta)
print(f"\n**instance_UpdatedInformalParserInterface es instancia de ParserMeta?:{ins} ")

# Creamos la implementaciones concretas pdf


class PdfParserNew:  # no es necesario definir explícitamente las subclases
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """
        Método que carga los datos fuente en un archivo PDF.
        :param path: Ruta de la ubicación del archivo PDF.
        :type path: str
        :param file_name: Nombre del archivo PDF.
        :type file_name: str
        :return: Cadena que representa el archivo PDF cargado.
        :rtype: str
        """
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """
        Método que extrae el texto de un archivo PDF.
        :param full_file_path: Ruta completa del archivo PDF.
        :type full_file_path: str
        :return: Diccionario que representa el texto extraído del archivo PDF.
        :rtype: dict
        """
        pass


print(f"\n\n--- type de PdfParserNew:{type(PdfParserNew)}")
t = issubclass(PdfParserNew, UpdatedInformalParserInterface)
print(f"\n**PdfParserNew es subclase de UpdatedInformalParserInterface?:{t} ")
n = isinstance(PdfParserNew, UpdatedInformalParserInterface)
print(f"\n**PdfParserNwe es instancia de UpdatedInformalParserInterface?:{n} ")

instance_PdfParser = PdfParserNew()
ins = isinstance(instance_PdfParser, PdfParserNew)
print(f"\n**instance_PdfParser es instancia de PdfParserNew?:{ins} ")
inst = isinstance(instance_PdfParser, UpdatedInformalParserInterface)
print(f"\n**instance_PdfParser es instancia de UpdatedInformalParserInterface?:{inst} ")


# Creamos la implementaciones concretas email ojo tiene un metodo distinto al de la interfaz


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source().

        Args:
        - path: str, ruta al directorio donde se encuentra el archivo
        - file_name: str, nombre del archivo

        Returns:
        - str, datos cargados en memoria
        """
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text().

        Args:
        - full_file_path: str, ruta completa al archivo

        Returns:
        - dict, texto extraído del correo electrónico
        """
        pass


print(f"\n\n--- type de EmlParserNew:{type(EmlParserNew)}")
l = issubclass(EmlParserNew, UpdatedInformalParserInterface)
print(f"\n**EmlParserNew es subclase de UpdatedInformalParserInterface?:{l} ")
j = isinstance(EmlParserNew, UpdatedInformalParserInterface)
print(f"\n**EmlParserNew es instancia de UpdatedInformalParserInterface?:{j} ")
instance_EmlParserNew = EmlParserNew()
inst = isinstance(instance_EmlParserNew, EmlParserNew)
print(f"\n**instance_EmlParserNew es instancia de EmlParserNew?:{inst} ")
ins = isinstance(instance_EmlParserNew, UpdatedInformalParserInterface)
print(
    f"\n**instance_EmlParserNew es instancia de UpdatedInformalParserInterface?:{ins} "
)
