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
print("Menu Inicio")
print("Opciones")
print("1 - Iniciar Sesion")
print("2 - Nuevo Usuario")

opcion_ingreso=int(input("Elegir Opcion: "))

if opcion_ingreso==1:
    correo_electronico=str(input("Correo Electronico:"))
    contraseña=str(input("Contraseña"))
    Inversor.loguin_usuario(correo_electronico,contraseña)
else:
    nuevo_inversor=Inversor("id_persona_cuit","id_billetera","nombre","id_localidad","ex_politica","id_inversor","calle","numero_calle","correo_electronico","contraseña")
    nuevo_inversor.alta_inversor()

#Probar Metodos


