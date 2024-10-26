from Conexion_MySQL import conectar_mysql
import mysql.connector

#Crear Clase Inversor
class Inversor:
    def __init__(self,correo_electronico,contraseña,id_inversor_cuit,id_perfil,id_billetera,nombre,
                 id_localidad,ex_politica,calle,numero_calle
                 ):
        self.id_inversor_cuit=id_inversor_cuit
        self.id_billetera=id_billetera
        self.id_perfil=id_perfil
        self.nombre=nombre
        self.id_localidad=id_localidad
        self.ex_politica=ex_politica
        self.calle=calle
        self.numero_calle=numero_calle
        self.correo_electronico=correo_electronico
        self.contraseña=contraseña
#Crear Metodos
    def nuevo_inversor(correo_electronico,contraseña,id_inversor_cuit,id_perfil,id_billetera,nombre,
                 id_localidad,ex_politica,calle,numero_calle):
        if conexion.is_connected:
            try:
                query= """INSERT INTO inversores (id_inversor,id_perfil,id_localidad,id_billetera,nombre,ex_plitica,calle,
                numero_calle,correo_electronico,contraseña) VALUES (id_inversor_cuit,id_localidad,id_billetera,
                nombre,ex_politica,calle,numero_calle,correo_electronico,contraseña)"""
                cursor.execute(query, (id_inversor_cuit,id_localidad,id_billetera,nombre,
                                        ex_politica,calle,numero_calle,correo_electronico,contraseña))
                conexion.commit()
                logger.info("Usuario registrado Satisfactoriamente. ")
            except mysql.connector.Error as err:
                logger.error(f"error al insertar {err}")
    
                
    #def baja()()
    #def editar()
    #def comprar()
    #def vender() 
    #def depositar()
    #def retirar()
    #def consulta_billetera()