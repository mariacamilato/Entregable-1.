from datetime import datetime 

class Implante:
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado):
        self.__marca=str
        self.__numPlaca=int
        self.__tipoImplante=str
        self.__tiempoVida=int
        self.__fecha=str
        self.__medico=str
        self.__estado=str

    def setMarca(self, marca):
        self.__marca=marca
    
    def setNumPlaca(self, numPlaca):
        self.__numPlaca=numPlaca
    
    def setTipoImplante(self, tipoImplante):
        self.__tipoImplante=tipoImplante
    
    def setTiempoVida(self,tiempoVida):
        self.__tiempoVida=tiempoVida
        
    
    def setFecha(self, fecha):
        self.__fecha=fecha
    
    def setMedico(self, medico):
        self.__medico=medico
    
    def setEstado(self, estado):
        self.__estado=estado
    
    def getMarca(self):
        return self.__marca
    
    def getNumPlaca(self):
        return self.__numPlaca
    
    def getTipoImplante(self):
        return self.__tipoImplante
    
    def getTiempoVida(self):
        return self.__tiempoVida
    
    def getFecha(self):
        return self.__fecha
    
    def getMedico(self):
        return self.__medico
    
    def getEstado(self):
        return self.__estado
    
class Implante_Cadera(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, material, tipoFijacion, tamaño):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado)
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
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, numElectrodos, alam, frecuencia):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado)
        self.__numElectrodos=numElectrodos
        self.__alam=alam
        self.__frecuencia=frecuencia

    def setNumElectrodos(self,numElectrodos):
        self.__numElectrodos=numElectrodos 
    
    def setAlam(self,alam):
        self.__alam=alam
    
    def setFrecuencia(self,frecuencia):
        self.__frecuencia=frecuencia
    
    def getNumElectrodos(self):
        return self.__numElectrodos
    
    def getAlam(self):
        return self.__alam
    
    def getFrecuencia(self):
        return self.__frecuencia 

class Stend_Coronario(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, longitud, diametro, material):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado)
        self.__longitud=longitud
        self.__diametro=diametro
        self.__material=material
    
    def setLongitud(self,longitud):
        self.__longitud=longitud
    
    def setDiametro(self,diametro):
        self.__diametro=diametro
    
    def setMaterial(self,material):
        self.__material=material

    def getLongitud(self):
        return self.__longitud
    
    def getDiametro(self):
        return self.__diametro

    def getMaterial(self):
        return self.__material 

class Implante_Rodilla(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, material, tipoFijacion, tamaño):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado)
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

class Paciente:
    def __init__(self, nombre, cedula, edad):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__edad=edad
        self.__listadoImplantes=[]

    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def setCedula(self, cedula):
        self.__cedula=cedula
    
    def setEdad(self, edad):
        self.__edad=edad
    
    def setListadoImplantes(self,lista):
        self.__listadoImplantes=lista
    
    def getNombre(self):
        return self.__nombre
    
    def getCedula(self):
        return self.__cedula
    
    def getEdad(self):
        return self.__edad
    
    def getListadoImplantes(self):
        return self.__listadoImplantes
           
class Sistema:
    def __init__(self):
        self.__listadoPacientes={}

    def agregarImplantes(self):
        self.implantes.append(Implante)

    def editarImplantes(self):
        pass

    def eliminarImplantes(self):
        pass

    def VerImplantes(self):
        pass
    
    








    
    





    

    
    
    
    
    

