# Crear Clase Operacion

class Operacion():
    def __init__(self,id_operacion,tipo_operacion,precio_operacion,fecha,id_inversor,id_accion):
        self.id_operacion=id_operacion
        self.tipo_operacion=tipo_operacion
        self.precio_operacion=precio_operacion
        self.fecha=fecha
        self.id_inversor=id_inversor
        self.id_accion=id_accion
#Crear metodos
    #def generar_orden