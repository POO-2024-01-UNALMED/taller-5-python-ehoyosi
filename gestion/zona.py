class Zona:
    def __init__(self,nombre=None,zoo=None,animales=None):
        self._nombre= nombre
        self._zoo= zoo
        if animales==None:
            self._animales=[]
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)
        animal.setZona(self)

    def cantidadAnimales(self):
        cantidad= len(self._animales)
        return cantidad
    
    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre

    def setZoo(self,zoo):
        self._zoo=zoo
    def getZoo(self):
        return self._zoo
    
    def setAnimales(self,animales):
        self._animales=animales
    def getAnimales(self):
        return self._animales