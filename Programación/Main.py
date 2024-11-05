from mod_Accion import Accion
from mod_Billetera import Billetera
from mod_Inversor import Inversor
from mod_Tablas_Grales import PerfilInversor, Provincia,Localidad, menu_inicio, menu_ingreso,lista_de_acciones
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
    elegir_operacion=int(input())
    if elegir_operacion<3:
        lista_de_acciones(id)
        if elegir_operacion==1:
            tipo_operacion="compra"
            id_inversor=int(id)
            id_accion=input("Elige Codigo Acción: ")
            cantidad=input("Ingresa la Cantidad a Operar: ")
            nueva_operacion=Operacion("id_operacion","tipo_operacion","precio_operacion","fecha","id_inversor","id_accion")
            nueva_operacion.generar_orden(tipo_operacion,id_inversor,id_accion,cantidad)
        else:
            tipo_operacion="compra"
            id_inversor=id
            id_accion=input("Elige Codigo Acción: ")
            cantidad=int(input("Ingresa la Cantidad a Operar: "))
            nueva_operacion=Operacion("id_operacion","tipo_operacion","precio_operacion","fecha","id_inversor","id_accion")
            nueva_operacion.generar_orden(tipo_operacion,id_inversor,id_accion,cantidad)
    elif elegir_operacion==3:
        billetera=Billetera()
        billetera.consultar_saldo(id)
    else: 
        id=0
        print("Vuelve a Iniciar el Sistema")





