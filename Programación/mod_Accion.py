#Crear clase Accion
class Accion():
    def __init__(self,id_accion,nombre_empresa,compra_diaria,venta_diaria,precio_venta,precio_compra,apertura,min_diario,
                max_diario,ultimo_cierre):
        self.id_accion=id_accion
        self.nombre_empresa=nombre_empresa
        self.compra_diaria=compra_diaria
        self.venta_diaria=venta_diaria
        self.precio_venta=precio_venta
        self.precio_compra=precio_compra
        self.__apertura=apertura
        self.min_diario=min_diario
        self.max_diario=max_diario
        self.ultimo_cierre=ultimo_cierre
        
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
        
    def edit_compra_diaria(self,nvo_compra_diaria):
        self.__compra_diaria=nvo_compra_diaria
        if self.compra_diaria==nvo_compra_diaria:
            return self.__compra_diaria
        else:
            return "La compra no pudo realizarce "
    
    def edit_venta_diaria(self,nvo_venta_diaria):
        self.__venta_diaria=nvo_venta_diaria
        if self.venta_diaria== nvo_venta_diaria:
            return self.__venta_diaria
        else:
            return "La venta no pudo Realizarce"
        
    def edit_apertura(self, nueva_apertura):
        self.apertura = nueva_apertura
        if self.apertura == nueva_apertura:
            return self.__apertura
        else:
            return "El precio no pudo Actualizarce"
        def mostrar_max_diario(self):
            return(f"El monto máximo diario es: {self.__max_diario}")
    
    def editar_max_diario(self,nvo_max_diario):
        self.__max_diario=nvo_max_diario
        return(f"Monto mínimo diario actualizado a: {self.__max_diario}")

#declarar metodo editar_min_diario
    def mostrar_min_diario(self):
        return (f"El mínimo diario es: {self.__min_diario}")
    
    def editar_min_diario(self,nvo_min_diario):
        self.__min_diario=nvo_min_diario
        return(f"Monto mínimo diario actualizado a: {self.__min_diario}")

#declarar metodo edit_min_diario
    def mostrar_ultimo_cierre(self):
        return(f"El monto del último cierre es: {self.__ultimo_cierre}")
    
    def editar_ultimo_cierre(self,nvo_ultimo_cierre):
        self.__ultimo_cierre=nvo_ultimo_cierre
        return(f"Monto del último cierre actualizado a: {self.__ultimo_cierre}")