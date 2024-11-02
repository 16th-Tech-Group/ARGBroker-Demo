from mod_Accion import Accion
from mod_Billetera import Billetera
from mod_Inversor import Inversor
from mod_Tablas_Grales import PerfilInversor, Provincia,Localidad
from mod_Operacion import Operacion
import Conexion_MySQL
import datetime
import mysql.connector
from mysql.connector import errorcode

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
opcion_ingreso=int(input("Elegir Opcion: "))

if opcion_ingreso==2:
    nuevo_inversor=Inversor("id_persona_cuit","id_billetera","nombre","id_localidad","ex_politica","calle","numero_calle","correo_electronico","contraseña")
    nuevo_inversor.alta_inversor()
else:
    correo_electronico=input("Correo Electronico: ")
    contraseña=input("Contraseña: ")
    ingreso=Inversor("id_persona_cuit","id_billetera","nombre","id_localidad","ex_politica","calle","numero_calle",correo_electronico,contraseña)
    ingreso.loguin_usuario(correo_electronico,contraseña)
    id=nuevo_inversor.imprimir_datos()
    print("----------------BIENVENIDO-----------------------")
    print("-------------------------------------------------")
    print("      ARG BROKER DEMO By 16th Tech Group "        )
    print("                                                 ")
    print("            Opciones de Usuario                  ")
    print("-------------------------------------------------")
    print("1 - Comprar")
    print("2 - Vender")
    print("3 - Consulta")
    print("-------------------------------------------------")   

#Probar Metodos


