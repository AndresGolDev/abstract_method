from abc import ABC, abstractmethod
class DispositivoMultimedia(ABC):
    def __init__(self, marca):
        self._marca = marca

    @property # = decorar los metodos  con la anotacion: propery
    def marca(self):
        return self._marca

    @marca.setter #anotaciones
    def marca(self, nueva_marca):
        self._marca = nueva_marca #modifica o actrualiza la informacion del atributo

    @abstractmethod #tiene metodos abstractos y se utiliza como
    def reproducir(self): # plantillas para otras clases
        pass

    @abstractmethod
    def detener(self):
        pass

    def mostrar_info(self):
        print(f"la Marca es: {self._marca}")

        """
        las clases normales no utilizan metodos abstractos 
        las clases abstractas tienen metodos abstractos y no se
         instancia directamente
        """

        """
        que es una clase abstracta: es aquella que tiene metodos abstractos 
                que no se puden instaciar directaMENTE  Y  sirve como
                plantillla para otras clases"""

        """metodo abstracto = es aquel que no tiene implementacion
        que es implementacion de un metodo: 
        """