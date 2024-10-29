from Conexion_MySQL import conectar_mysql
#Crear clase Accion
class Accion():
    def __init__(self,id_accion,nombre_empresa,compra_diaria,venta_diaria,precio_venta,precio_compra,apertura,min_diario,
                max_diario,ultimo_cierre):
        self.__id_accion=id_accion
        self.__nombre_empresa=nombre_empresa
        self.__compra_diaria=compra_diaria
        self.__venta_diaria=venta_diaria
        self.__precio_venta=precio_venta
        self.__precio_compra=precio_compra
        self.__apertura=apertura
        self.__min_diario=min_diario
        self.__max_diario=max_diario
        self.__ultimo_cierre=ultimo_cierre
        
#Creacion de Getters y Setters
    def get_compra_diaria(self):
        return self.__compra_diaria
    def set_compra_diaria(self,compra_diaria):
        self.__compra_diaria = compra_diaria
        
    def get_venta_diaria(self):
        return self.__venta_diaria
    def set_venta_diaria(self,venta_diaria):
        self.__venta_diaria = venta_diaria
    
    def get_apertura(self):
        return self.__apertura
    def set_apertura(self,apertura):
        self.__apertura = apertura
        
    def get_precio_venta(self):
        return self.__precio_venta
    def set_precio_venta(self,precio_venta):
        self.__precio_venta = precio_venta
        
    def get_precio_compra(self):
        return self.__precio_compra
    def set_precio_compra(self,precio_compra):
        self.__precio_compra = precio_compra
        
#Creacion de los metodos
    
    def edit_compra_diaria(self,compra_diaria):
        self.__compra_diaria=compra_diaria
        if self.__compra_diaria==compra_diaria:
            return self.__compra_diaria
        else:
            return "La compra no pudo realizarce"
    
    def edit_venta_diaria(self,nvo_venta_diaria):
        self.__venta_diaria=nvo_venta_diaria
        if self.__venta_diaria== nvo_venta_diaria:
            return self.__venta_diaria
        else:
            return "La venta no pudo Realizarce"
        
    def edit_apertura(self,apertura):
        self.__apertura = apertura
        if self.__apertura == apertura:
            return self.__apertura
        else:
            return "El precio no pudo Actualizarce"
        
    def mostrar_max_diario(self):
        monto = conectar_mysql(Orden = "select max_diario from Acciones")
        return monto
    
    def editar_max_diario(self,nvo_max_diario):
        self.__max_diario=nvo_max_diario
        return(f"Monto mínimo diario actualizado a: {self.__max_diario}")

#declarar metodo editar_min_diario
    def mostrar_min_diario(self):
        monto = conectar_mysql(Orden = "select min_diario from Acciones")
        return monto
    
    def editar_min_diario(self,nvo_min_diario):
        self.__min_diario=nvo_min_diario
        return(f"Monto mínimo diario actualizado a: {self.__min_diario}")

#declarar metodo edit_min_diario
    def mostrar_ultimo_cierre(self):
        monto = conectar_mysql(Orden = "select ultimo_cierre from Acciones")
        return monto
    
    def editar_ultimo_cierre(self,nvo_ultimo_cierre):
        self.__ultimo_cierre=nvo_ultimo_cierre
        return(f"Monto del último cierre actualizado a: {self.__ultimo_cierre}")