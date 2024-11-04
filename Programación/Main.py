from mod_Accion import Accion
from mod_Billetera import Billetera
from mod_Inversor import Inversor
from mod_Tablas_Grales import PerfilInversor, Provincia,Localidad, menu_inicio, menu_ingreso
from mod_Operacion import Operacion
import Conexion_MySQL
import datetime
import mysql.connector
from mysql.connector import errorcode
from Conexion_MySQL import conectar_mysql

menu_inicio()
opcion_ingreso=int(input("Elegir Opcion: "))

if opcion_ingreso==2:
    nuevo_inversor=Inversor("id_persona_cuit","id_billetera","nombre","id_localidad","ex_politica","calle","numero_calle","correo_electronico","contraseña")
    nuevo_inversor.alta_inversor()
else:
    correo_electronico=input("Correo Electronico: ")
    contraseña=input("Contraseña: ")
    ingreso=Inversor("id_persona_cuit","id_billetera","nombre","id_localidad","ex_politica","calle","numero_calle",correo_electronico,contraseña)
    ingreso.loguin_usuario(correo_electronico,contraseña)
    id=conectar_mysql("SELECT id_persona_cuit FROM inversores WHERE correo_electronico = ('{0}')".format(correo_electronico))
    id=(id[0][0])
    menu_ingreso()
    saldo=(conectar_mysql("SELECT saldo_ars FROM billeteras WHERE id_persona_cuit = ('{0}')".format(id)))
    saldo=(saldo[0][0])
    print("-------------------------------------------------") 
    print("Saldo en Efectivo:   $       "+str(saldo))
    print("-------------------------------------------------")
    print("Elegi la Operación a realizar: ") 
#Probar Metodos


