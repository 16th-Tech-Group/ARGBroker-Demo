#Creacion de la clase Billetera
class Billetera:
    def __init__(self,id_billetera,id_accion,cantidad_accion,valor_promedio,
                 nombre_accion,cantidad_dinero,total_invertido,ganacia,
                 perdidas,id_operacion):
        self.__id_billetera = id_billetera
        self.__id_accion = id_accion
        self.__cantidad_accion = cantidad_accion
        self.__valor_promedio = valor_promedio
        self.__nombre_accion = nombre_accion
        self.__cantidad_dinero = cantidad_dinero
        self.__total_invertido = total_invertido
        self.__ganacia = ganacia
        self.__perdidas = perdidas
        self.__id_operacion = id_operacion

##heyme coraspe