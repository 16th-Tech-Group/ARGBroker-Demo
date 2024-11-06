from Conexion_MySQL import conectar_mysql
#Creacion de la clase Billetera
class Billetera:
    def __init__(self,id_billetera,id_accion,cantidad_accion,valor_promedio,
                 nombre_accion,cantidad_dinero,total_invertido,ganancia,
                 perdidas,id_operacion):
        self.__id_billetera = id_billetera
        self.__id_accion = id_accion
        self.__cantidad_accion = cantidad_accion
        self.__valor_promedio = valor_promedio
        self.__nombre_accion = nombre_accion
        self.__cantidad_dinero = cantidad_dinero
        self.__total_invertido = total_invertido
        self.__ganancia = ganancia
        self.__perdidas = perdidas
        self.__id_operacion = id_operacion
#Dar de alta la billetera en la Base de Datos   
    def alta_billetera(self,id_persona_cuit):
        orden="INSERT INTO billeteras (id_persona_cuit) VALUES (%s);"
        valor=[id_persona_cuit]
        conectar_mysql(orden,valor)
    def consultar_saldo(self,id_persona_cuit):
        conectar_mysql(f"SELECT id_accion, SUM(cantidad),PROM(precio_venta) FROM acciones WHERE id_persona_cuit={id_persona_cuit}")
