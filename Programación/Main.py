from mod_Accion import Accion
from mod_Billetera import Billetera
from mod_Inversor import Inversor
from mod_Tablas_Grales import PerfilInversor, Provincia,Localidad
from mod_Operacion import Operacion
import Conexion_MySQL
import datetime

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
    id_persona_cuit=input("Cuit: ")
    id_billetera="SELECT COUNT(id_billetera) FROM Billeteras"
    id_billetera=Conexion_MySQL.conectar_mysql(id_billetera)
    id_billetera=int(id_billetera[0][0])+1
    print(id_billetera)
    nombre=input("Nombre: ")
    id_localidad=input("Localidad:")
    id_localidad="SELECT id_localidad FROM Localidades WHERE nombre_localidad= '{id_localidad}';"
    id_localidad=Conexion_MySQL.conectar_mysql(id_localidad)
    ex_politica=input("¿Es ud una Persona Expuesta Politicamente: ")
    id_inversor="SELECT COUNT(*) FROM Inversores"
    id_inversor=Conexion_MySQL.conectar_mysql(id_inversor)
    calle=input("Calle: ")
    numero_calle=input("N°: ")
    correo_electronico=input("Usuario (Ingrese Correo Electronico: ")
    contraseña=input("Ingrese una contraseña")
    contraseña2=input("Confirme Contraseña: ")
    while contraseña!=contraseña2:
        contraseña=input("Ingrese una contraseña")
        contraseña2=input("Confirme Contraseña: ")
    
    nuevo_inversor=Inversor.alta_inversor(self=id_inversor)

#Probar Metodos


