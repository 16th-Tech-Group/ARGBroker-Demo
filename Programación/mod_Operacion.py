# Crear Clase Operacion
import datetime
from Conexion_MySQL import conectar_mysql

class Operacion():
    def __init__(self,id_operacion,tipo_operacion,precio_operacion,fecha,id_inversor,id_accion):
        self.__id_operacion=id_operacion
        self.__tipo_operacion=tipo_operacion
        self.__precio_operacion=precio_operacion
        self.__fecha=fecha
        self.__id_inversor=id_inversor
        self.__id_accion=id_accion

#getter y setter

    def get_id_operacion(self):
        return self.__id_operacion
    def set_id_persona_cuit(self,id_operacion):
        self.__id_operacion = id_operacion

    def get_tipo_operacion(self):
        return self.__tipo_operacion
    def set_id_persona_cuit(self,tipo_operacion):
        self.__tipo_operacion = tipo_operacion    
    
    def get_precio_operacion(self):
        return self.__precio_operacion
    def set_precio_operacion(self,precio_operacion):
        self.__id_operacion = precio_operacion   

    def get_fecha(self):
        return self.__fecha
    def set_fecha(self,fecha):
        self.__fecha = fecha   

    def get_id_inversor(self):
        return self.__id_inversor
    def set_id_inversor(self,id_inversor):
        self.__id_inversor = id_inversor      

    def get_id_accion(self):
        return self.__id_accion
    def set_id_accion(self,id_accion):
        self.__id_accion = id_accion     


#Crear metodo generar_orden
    def generar_orden(self,tipo_operacion,id_inversor,id_accion,cantidad):
        cant_id_inversor=conectar_mysql(Orden="SELECT SUM(cantidad_accion) FROM operaciones WHERE id_inversor=%s AND id_accion=%s GROUP BY id_accion",Valores=(id_inversor,id_accion))
        saldo_inversor=conectar_mysql("SELECT saldo_ars FROM billeteras WHERE id_inversor=({0}),format(id_inversor)".format(id_inversor))
        fecha=datetime.date.today()
        if tipo_operacion == "compra":
            precio_operacion=conectar_mysql("SELECT precio_compra FROM Acciones WHERE id_accion=({0})".format(id_accion))
            precio_operacion=int(precio_operacion[0][0])
            if precio_operacion*cantidad>saldo_inversor:
                print("No tiene saldo para efectuar la operacion")
            else:
                operacion=conectar_mysql("INSERT INTO operaciones (tipo_operacion,precio_operacion,fecha,id_inversor,id_accion) VALUES (%s,%s,%s,%s,%s))")
                valores=[tipo_operacion,precio_operacion,fecha,id_inversor,id_accion]
                conectar_mysql(operacion=operacion, valores=valores)
                print("Operacion realizada con exito")
        else: 
            precio_operacion=conectar_mysql("SELECT precio_compra FROM Acciones WHERE id_accion=({0})".format(id_accion))
            precio_operacion=int(precio_operacion[0][0])
            if cantidad<cant_id_inversor:
                return "Cantidad de acciones insuficiente para efectuar la operacion"
            else:
                operacion="INSERT INTO operaciones (tipo_operacion,precio_operacion,fecha,id_inversor,id_accion) VALUES (%s,%s,%s,%s,%s))"
                conectar_mysql(operacion=operacion, valores=valores)
                return "Operacion realizada con exito"
