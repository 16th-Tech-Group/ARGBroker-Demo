from Conexion_MySQL import conectar_mysql
# Crear Clases Generales
class PerfilInversor():
    def __init__(self,id_tipo_inversor,tipo_inversor):
        self.id_tipo_inversor=id_tipo_inversor
        self.tipo_inversor=tipo_inversor
#Declarar Metodos

class Provincia:
    def __init__(self,id_provincia,nombre_provincia):
        self.__id_provincia=id_provincia
        self.__nombre_provincia=nombre_provincia
 #Declarar Metodos
    def get_id_provincia(self):
        return self.__id_provincia
    def set_id_provincia(self):
        return self.id_provincia
    
    def get__nombre_provincia(self):
        return self.__nombre_provincia
    def set___nombre_provincia(self):
        return self.__nombre_provincia
#CREAR METODOS: AGREGAR, EDITAR, ELIMINAR  (CLASES LOCALIDAD Y PROVINCIA)
#metodo editar_provincia
    def editar_nombre_provincia(self,provincia_editada):
        self.__nombre_provincia=provincia_editada
        return(f"El nombre de la provincia se actualizó: {self.__nombre_provincia}")
 
#############################################################################################
class Localidad:
    def __init__(self,id_localidad,id_provincia,nombre_localidad):
        self.__id_localidad=id_localidad
        self.__id_provincia=id_provincia
        self.__nombre_localidad=nombre_localidad
    
    def get__id_localidad(self):
        return self.__id_localidad
    def set__id_localidad(self):
        return self.id_localidad
    
    def get__nombre_localidad(self):
        return self.__nombre_localidad
    def set__nombre_localidad(self):
        return self.__nombre_localidad 
#CREAR METODOS: AGREGAR, EDITAR, ELIMINAR  (CLASES LOCALIDAD Y PROVINCIA)
#metodo editar_localidad
    def editar_localidad(self,localidad_editada):
        self.__nombre_localidad=localidad_editada
        return(f"El nombre de la localidad se actualizó: {self.__nombre_localidad}")
    
