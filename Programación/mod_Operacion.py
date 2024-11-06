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
        id_billetera=conectar_mysql(f"SELECT id_billetera from billeteras WHERE id_persona_cuit={id_inversor}")
        cant_id_inversor=conectar_mysql(Orden=f"SELECT SUM(cantidad_accion) FROM operaciones WHERE id_billetera={id_billetera[0][0]} AND id_accion='{id_accion}'")
        if cant_id_inversor[0][0]==None:
            cant_id_inversor=0
        else:  
            cant_id_inversor=(cant_id_inversor[0][0])
        saldo_inversor=conectar_mysql(f"SELECT saldo_ars FROM billeteras WHERE id_billetera={id_billetera[0][0]}")
        fecha=datetime.datetime.now()
        if tipo_operacion == "compra":
            precio_operacion=conectar_mysql(f"SELECT precio_compra FROM Acciones WHERE id_accion='{id_accion}'")
            precio_operacion=float(precio_operacion[0][0])
            comision=precio_operacion*float(cantidad)*float(0.015)
            costo_operacion=precio_operacion*int(cantidad)+comision
            if costo_operacion>=int(saldo_inversor[0][0]):
                print("No tiene saldo para efectuar la operacion")
            else:
                operacion="INSERT INTO operaciones (tipo_operacion,precio_operacion,cantidad_accion,fecha,id_billetera,id_accion,monto_comision) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                valores=[tipo_operacion,precio_operacion,cantidad,fecha,id_billetera[0][0],id_accion,comision]
                print(valores)
                conectar_mysql(Orden=operacion, Valores=valores)
                saldo_inversor=saldo_inversor[0][0]-costo_operacion
                conectar_mysql("UPDATE billeteras SET saldo_ars=%s WHERE id_billetera=%s",[saldo_inversor,id_billetera[0][0]])
                print("Operacion realizada con exito")
        else: 
            precio_operacion=conectar_mysql(f"SELECT precio_venta FROM Acciones WHERE id_accion='{id_accion}'")
            precio_operacion=float(precio_operacion[0][0])
            comision=precio_operacion*float(cantidad)*float(0.015)
            ingreso=precio_operacion*float(cantidad)-comision       
            if int(cantidad)>=cant_id_inversor:
                print("Cantidad de acciones insuficiente para efectuar la operacion")
            else:
                cantidad=cantidad*-1
                operacion="INSERT INTO operaciones (tipo_operacion,precio_operacion,cantidad_accion,fecha,id_billetera,id_accion,monto_comision) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                valores=[tipo_operacion,precio_operacion,cantidad,fecha,id_billetera[0][0],id_accion,comision]
                conectar_mysql(Orden=operacion, Valores=valores)
                saldo_inversor=saldo_inversor[0][0]+ingreso
                conectar_mysql("UPDATE billeteras SET saldo_ars=%s WHERE id_billetera=%s",[saldo_inversor,id_billetera[0][0]])
                print("Operacion realizada con exito")
