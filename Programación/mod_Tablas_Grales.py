from Conexion_MySQL import conectar_mysql
from mod_Billetera import Billetera
from prettytable import PrettyTable
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
#metodo aeditar_localidad
    def editar_localidad(self,localidad_editada):
        self.__nombre_localidad=localidad_editada
        return(f"El nombre de la localidad se actualizó: {self.__nombre_localidad}")
    
def menu_inicio():
    #Menu opciones
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("Bienvenidos a ARG BROKER DEMO By 16th Tech Group ")
    print("                Menu Inicio                      ")
    print("            Opciones de Inicio                   ")
    print("-------------------------------------------------")
    print("1 - Iniciar Sesion")
    print("2 - Nuevo Usuario")
    print("-------------------------------------------------")

#Ingreso
def menu_ingreso():
    print("----------------BIENVENIDO-----------------------")
    print("-------------------------------------------------")
    print("      ARG BROKER DEMO By 16th Tech Group "        )
    print("                                                 ")
    print("            Opciones de Usuario                  ")
    print("-------------------------------------------------")
    print("1 - Comprar")
    print("2 - Vender")
    print("3 - Consulta INVERSIONES")
    print("4 - Cerrar Sesión")
    print("-------------------------------------------------") 

def lista_de_acciones(valores):
    print("----------------OPERACIONES DE COMPRA------------")
    print("                 VALORES NEGOCIADOS")
    tabla= PrettyTable()
    tabla.add_column("Codigo",conectar_mysql(Orden="SELECT id_accion from acciones"),)
    tabla.add_column("Nombre de la Empresa",conectar_mysql(Orden="SELECT nombre_empresa from acciones"),)
    tabla.add_column("Precio de Venta",conectar_mysql(Orden="SELECT precio_venta from acciones"),)
    tabla.add_column("Precio de Compra",conectar_mysql(Orden="SELECT precio_compra from acciones"),)
    print("-------------------------------------------------")
    print(tabla)
    print("      ARG BROKER DEMO By 16th Tech Group "        )
