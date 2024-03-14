
class Implante:
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, disponibilidad):
        self.__marca=str
        self.__numPlaca=int
        self.__tipoImplante=str
        self.__tiempoVida=int
        self.__fecha=str
        self.__medico=str
        self.__estado=str
        self.__disponibilidad=str 

    def setMarca(self, marca):
        self.__marca=marca
    
    def setNumPlaca(self, numPlaca):
        self.__numPlaca=numPlaca
    
    def setTipoImplante(self, tipoImplante):
        self.__tipoImplante=tipoImplante
    
    def setTiempoVida(self,tiempoVida):
        self.__tiempoVida=tiempoVida
    
    def setDisponibilidad(self,dis):
        self.__disponibilidad = dis 
        
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
    
    def getDisponibilidad(self):
        return self.__disponibilidad
    
class Implante_Cadera(Implante):
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, material, tipoFijacion, tamaño, disponibilidad):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, disponibilidad)
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
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, numElectrodos, alam, frecuencia, disponibilidad):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, disponibilidad)
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
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, longitud, diametro, material, disponibilidad):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, disponibilidad)
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
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, material, tipoFijacion, tamaño, disponibilidad):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, fecha, medico, estado, disponibilidad)
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
    def __init__(self, marca, numPlaca, tipoImplante, tiempoVida, forma, sistemaFijacion, material, disponibilidad):
        Implante.__init__(self, marca, numPlaca, tipoImplante, tiempoVida, disponibilidad)
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
    def __init__(self):
        self.__nombre=""
        self.__cedula=""
        self.__edad=""
        self.__fecha= ""
        self.__listadoImplantes=[]
    
    def setFecha(self, fecha):
        self.__fecha = fecha

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
    
    def getFecha(self):
        return self.__fecha
           
class Sistema:
    def __init__(self):
        self.__listadoPacientes={}
        self.__inventarioImplantes={}

    def agregarPaciente(self,id,paciente):
        self.__listadoPacientes[id] = paciente

    def agregarImplantes(self,placa,info):
        self.__inventarioImplantes[placa] = info
        
    def verificarImplante(self,placa):
        for k, v in self.__inventarioImplantes.items():
            if k == placa:
                return True
            
    def verificarPaciente(self,id):
        for k,v in self.__listadoPacientes.items():
            if v.getCedula() == id:
                return True

    def setInfoGeneralImplante(self,placa):
        marca = input("Ingrese la marca: ")
        tiempo_vida = input("Ingrese la vida util del implante: ")
        fecha = input("Ingrese la fecha de registro: ")
        medico = input("Ingrese el medico responsable: ")
        estado = input("Ingrese el estado del implante: ")
        
        self.__inventarioImplantes[placa].setMarca(marca)
        self.__inventarioImplantes[placa].setTiempoVida(tiempo_vida)
        self.__inventarioImplantes[placa].setFecha(fecha)
        self.__inventarioImplantes[placa].setMedico(medico)
        self.__inventarioImplantes[placa].setEstado(estado)

    def eliminarImplantes(self,placa):
        self.__inventarioImplantes.pop(placa)

    def verPacientes(self,id):
        for k,v in self.__listadoPacientes.items():
            if k == id:
                print(f'''
                Nombre: {v.getNombre()}
                Edad: {v.getEdad()}
                cedula: {v.getCedula()}
                Fecha de implantacion: {v.getFecha()}
                ''')    
                print("Placas de los implantes asignados:")
               
                for x in range(len(v.getListadoImplantes())):
                    print(v.getListadoImplantes()[x])
        return k,v

    def getImplantes(self):
        dic = {}
        for k,v in self.__inventarioImplantes.items():
            if v.getDisponibilidad() == "Disponible":
                dic[k] = v 
        return dic
    
    def editDisponibilidad(self,placa):
        for k, v in self.__inventarioImplantes.items():
            if k == placa:
                v.setDisponibilidad(" ¡¡¡ No disponible !!!")

    def verImplantesDisponibles(self):
        lista = []
        for x in self.VerImplantes():
            if self.__inventarioImplantes[x].getDisponibilidad() == "Disponible":
                lista.append(x)
        return lista

    def VerImplantes(self):
        lista = []
        for k,v in self.__inventarioImplantes.items():
            lista.append(k)
            print(f'''
            Numero de placa: {k}                              
            Tipo de implante: {v.getTipoImplante()}
            Marca: {v.getMarca()}
            fecha de ingreso: {v.getFecha()}
            tiempo de vida: {v.getTiempoVida()}
            Estado: {v.getEstado()}
            Medico responsable: {v.getMedico()}
            Disponibilidad: {v.getDisponibilidad()}
            ''')
            if v.getTipoImplante() == "Marcapasos":
                print(f'''
            Numero de electrodos: {v.getNumElectrodos()}
            Tipo de señal: {v.getAlam()}
            Frecuencia: {v.getFrecuencia()}
            **********************************''')
            
            elif v.getTipoImplante() == "Stend Coronario":
                print(f'''
            Longitud: {v.getLongitud()}
            Diametro: {v.getDiametro()}
            Tipo de Material: {v.getMaterial()}
            **********************************''')
            
            else:
                print(f'''
            Tipo de material: {v.getMaterial()}
            Sistema de fijacion: {v.getTipoFijacion()}
            Tamaño: {v.getTamaño()}
            **********************************''')
        return(lista)             
    
def main():
    sistema = Sistema()
    while True:
        menu=input('''\nSeleccione: 
                   \n1. Registro de pacientes y asignacion de implantes
                   \n2. Registro y modificacion de implantes
                   \n3. Salir 
                   \n>>>''')
        
        if menu == "1":
    
            menu=input('''\nMenu de pacientes
                    \nSeleccione: 
                    \n1. Ingresar un nuevo paciente
                    \n2. Buscar un paciente por su ID
                    \n3. Salir 
                    \n>>>''')
            
    

    
    








    
    





    

    
    
    
    
    

