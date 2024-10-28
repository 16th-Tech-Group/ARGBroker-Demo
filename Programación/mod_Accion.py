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
#Creacion de getters y setters
    def get_compra_diaria(self):
        return self.__compra_diaria
    def set_compra_diaria(self,compra_diaria):
        self.__compra_diaria = compra_diaria
        
    def get_venta_diaria(self):
        return self.__venta_diaria
    def set_venta_diaria(self,venta_diaria):
        self.__venta_diaria = venta_diaria
        
    def get_precio_venta(self):
        return self.__precio_venta
    def set_precio_venta(self,precio_venta):
        self.__precio_venta = precio_venta
    
    def get_precio_compra(self):
        return self.__precio_compra
    def set_precio_compra(self,precio_compra):
        self.__precio_compra = precio_compra
    
    def get_apertura(self):
        return self.__apertura
    def set_apertura(self,apertura):
        self.__apertura = apertura
        
    def get_min_diario(self):
        return self.__min_diario
    def set_min_diario(self,min_diario):
        self.__min_diario = min_diario
        
    def get_max_diario(self):
        return self.__max_diario
    def set_max_diario(self,max_diario):
        self.__max_diario = max_diario
    
    def get_ultimo_cierre(self):
        return self.__ultimo_cierre
    def set_ultimo_cierre(self,ultimo_cierre):
        self.__ultimo_cierre = ultimo_cierre
    

#Declarar Metodos
    #def alta_accion(self):
    #def baja_accion(self):
    def edit_compra_diaria(self,nvo_compra_diaria):
        self.set_compra_diaria=nvo_compra_diaria
        return "Compra diaria actualizada a:",self.get_compra_diaria
    
    def edit_venta_diaria(self,nvo_venta_diaria):
        self.set_venta_diaria=nvo_venta_diaria
        return "Venta diaria actualizada a:",self.get_venta_diaria
    
    