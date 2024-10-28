# Crear Clase Operacion
import datetime

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
    def generar_orden(tipo_operacion,id_inversor,id_accion,cantidad):
        tipo_operacion=input("Ingrese 1 si quiere comprar o 2 si quiere vender:")
        cant_id_inversor= "SELECT SUM(*) FROM operaciones WHERE id_inversor=%s AND id_accion=%s"
        saldo_inversor="SELECT saldo_ars FROM billeteras WHERE id_inversor=%s"
        id_operacion="SELECT COUNT(*) FROM operaciones"
        id_operacion=id_operacion+1
        fecha=datetime.date.today()
        if tipo_operacion == "compra":
            precio_operacion="SELECT precio_compra FROM Acciones WHERE id_accion=%s"
            if precio_operacion*cantidad>saldo_inversor:
                print("No tiene saldo para efectuar la operacion")
            else:
                operacion="INSERT INTO operaciones (id_operacion,tipo_operacion,precio_operacion,fecha,id_inversor,id_accion) VALUES (%s,%s,%s,%s,%s,%s))"
                valores=[id_operacion,tipo_operacion,precio_operacion,fecha,id_inversor,id_accion]
                conectar_mysql(operacion=operacion, valores=valores)
                print("Operacion realizada con exito")
        else: 
            precio_operacion="SELECT precio_venta FROM Acciones WHERE id_accion=%s"
            if cantidad<cant_id_inversor:
                return "Cantidad de acciones insuficiente para efectuar la operacion"
            else:
                operacion="INSERT INTO operaciones (id_operacion,tipo_operacion,precio_operacion,fecha,id_inversor,id_accion) VALUES (%s,%s,%s,%s,%s,%s))"
                conectar_mysql(operacion=operacion, valores=valores)
                return "Operacion realizada con exito"




