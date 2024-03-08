class Implante:
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida):
        self.__marca=str
        self.__numPlaca=int
        self.__tipoImplante=str
        self.__tiempoVida=int

    def setMarca(self, marca):
        self.__marca=marca
    
    def setNumPlaca(self, numPlaca):
        self.__numPlaca=numPlaca
    
    def setTipoImplante(self, tipoImplante):
        self.__tipoImplante=tipoImplante
    
    def setTiempoVida(self,tiempoVida ):
        self.__tiempoVida=tiempoVida
    
    def getMarca(self):
        return self.__marca
    
    def getNumPlaca(self):
        return self.__numPlaca
    
    def getTipoImplante(self):
        return self.__tipoImplante
    
    def getTiempoVida(self):
        return self.__tiempoVida
    
class Implante_Cadera(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, material, tipoFijacion, tamaño):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida)
        self.__material=material
        self.__tipoFijacion=tipoFijacion
        self.__tamaño=tamaño
    
    def setMaterial(self,material):
        self.__material=material 

    def setTipoFijacion(self, tipoFijacion):
        self.__tipoFijacion=tipoFijacion
    
    def setTamaño(self, tamaño):
        self.__tamaño=tamaño
    
    def getMaterial(self):
        return self.__material
    
    def getTipoFijacion(self):
        return self.__tipoFijacion
    
    def getTamaño(self):
        return self.__tamaño

class Marcapasos(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, numElectrodos, alam, frecuencia):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida)
        self.__numElectrodos=numElectrodos
        self.__alam=alam
        self.__frecuencia=frecuencia

    def setNumElectrodos(self,numElectrodos):
        self.___numElectrodos=numElectrodos 
    
    def setAlam(self,alam):
        self.__alam=alam
    
    def setFrecuencia(self,frecuencia):
        self.__frecuencia=frecuencia
    
    def getNumElectrodos(self):
        return self.___numElectrodos
    
    def getAlam(self):
        return self.___alam
    
    def getFrecuencia(self):
        return self.__frecuencia 

class Stend_Coronario(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, longitud, diametro, material):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida)
        self.__longitud=longitud
        self.___diametro=diametro
        self.__material=material
    
    def setLongitud(self,longitud):
        self.__longitud=longitud
    
    def setDiametro(self,diametro):
        self.___diametro=diametro
    
    def setMaterial(self,material):
        self.___material=material

    def getLongitud(self):
        return self.__longitud
    
    def getDiametro(self):
        return self.___diametro

    def getMaterial(self):
        return self.___material 

class Implante_Rodilla(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, material, tipoFijacion, tamaño):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida)
        self.__material=material
        self.__tipoFijacion=tipoFijacion
        self.__tamaño=tamaño
    
    def setMaterial(self,material):
        self.__material=material 

    def setTipoFijacion(self, tipoFijacion):
        self.__tipoFijacion=tipoFijacion
    
    def setTamaño(self, tamaño):
        self.__tamaño=tamaño
    
    def getMaterial(self):
        return self.__material
    
    def getTipoFijacion(self):
        return self.__tipoFijacion
    
    def getTamaño(self):
        return self.__tamaño

class Implante_Dental(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, forma, sistemaFijacion, material):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida)
        self.__forma=forma
        self.__sistemaFijacion=sistemaFijacion
        self.__material=material  
    
    def setForma(self,forma):
        self.__forma=forma
    
    def setSistemaFijacion(self, sistemaFijacion):
        self.__sistemaFijacion=sistemaFijacion
    
    def setMaterial(self, material):
        self.__material=material
    
    def getForma(self):
        return self.__forma
    
    def getSistemaFijacion(self):
        return self.__sistemaFijacion
    
    def getMaterial(self):
        return self.__material

class Sistema:
    def __init__(self):
        self.__listadoImplantes=[]
    
    








    
    





    

    
    
    
    
    

