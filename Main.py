from Conexion_MySQL import conectar_mysql
from mod_Inversor import Inversor

conexion=conectar_mysql()


if conexion.is_connected:
    #crear cursor
    cursor=conexion.cursor()

#Menu opciones
print("Menu Inicio")
print("Opciones")
print("1 - Inicial Sesion")
print("2 - Nuevo Usuario")
opcion_elegida=int(input("Elegir Opcion (1 o 2) que corresponda:"))
id_billetera=0

if opcion_elegida==2:
    correo_electronico=input("Ingrese correo electronico: ")
    contraseña=input("Ingrese contraseña: ")
    id_inversor_cuit=input("Ingrese Cuit o Cuil: ")
    id_billetera=id_billetera+1
    nombre=input("ingrese Nombre y Apellido o Razon Social: ")
    id_localidad=input("Ingrese Localidad: ")
    ex_politica=input("¿Es Usted una persona Expuesta Politicamente")
    calle=input("Calle")
    numero_calle=input("altura")
    id_perfil=input("Tipo de Perfil: ")

    id_inversor_cuit=Inversor(str(correo_electronico),str(contraseña),str(id_inversor_cuit),str(id_perfil),str(id_billetera),
                              nombre,str(id_localidad),str(ex_politica),str(calle),str(numero_calle))
    
    id_inversor_cuit.nuevo_inversor()
else: 
    print("Login Usuario")


