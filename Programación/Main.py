from mod_Accion import Accion
from mod_Billetera import Billetera
from mod_Inversor import Inversor
from mod_Tablas_Grales import PerfilInversor, Provincia,Localidad
from mod_Operacion import Operacion
import datetime

#Menu opciones
print("Menu Inicio")
print("Opciones")
print("1 - Inicial Sesion")
print("2 - Nuevo Usuario")
opcion_ingreso=input("Elegir Opcion: ")

if opcion_ingreso==1:
    correo_electronico=str(input("Correo Electronico:"))
    contraseña=str(input("Contraseña"))
    Inversor.loguin_usuario(correo_electronico,contraseña)
else:
    id_persona_cuit=input("Cuit: ")
    id_billetera="SELECT COUNT(*) FROM Billetera"
    id_billetera=conectar_mysql(id_billetera)+1
    nombre=input("Nombre: ")
    id_localidad=input("Localidad:")
    id_localidad="SELECT id_localidad FROM Localidades WHERE localidad= '{id_localidad}';"
    id_localidad=conectar_mysql(id_localidad)
    ex_politica=input("¿Es ud una Persona Expuesta Politicamente: ")
    id_inversor="SELECT COUNT(*) FROM Inversor"
    id_inversor=conectar_mysql(id_inversor)
    calle=input("Calle: ")
    numero_calle=input("N°: ")
    correo_electronico=input("Usuario (Ingrese Correo Electronico: ")
    contraseña=input("Ingrese una contraseña")
    contraseña2=input("Confirme Contraseña: ")
    while contraseña==contraseña2:
        Inversor.alta_inversor(id_persona_cuit,id_billetera,nombre,id_localidad,ex_politica,id_inversor,calle,numero_calle,correo_electronico,contraseña)


#Probar Metodos


