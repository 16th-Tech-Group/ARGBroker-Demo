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
        self.apertura=apertura
        self.min_diario=min_diario
        self.max_diario=max_diario
        self.ultimo_cierre=ultimo_cierre
        
    def alta_accion(self,id_accion,nombre_empresa,compra_diaria,venta_diaria,precio_compra,precio_venta,apertura,min_diario,max_diario,ultimo_cierre)
        self.id_accion=id_accion
        self.nombre_empresa=nombre_empresa
        self.compra_diaria=compra_diaria
        self.venta_diaria = venta_diaria
        self.precio_compra=precio_compra
        self.precio_venta=precio_venta
        self.apertura=apertura
        self.min_diario=min_diario
        self.max_diario=max_diario
        self.ultimo_cierre=ultimo_cierre
    
    def baja_accion(self):
        self.id_accion=None
        self.nombre_empresa=None
        self.compra_diaria=0
        self.venta_diaria=0
        self.precio_venta=0
        self.precio_compra=0
        self.apertura=0
        self.min_diario=0
        self.max_diario=0
        self.ultimo_cierre=0
        return (f"accion dada de baja")
#Declarar Metodos
        def variaciacion_diaria(self):
            if self.apertura==0:
                return 0
        return ((self.ultimo_cierre - self.apertura) /self.apertura ) *100
    
        def promedio_precio_transacciones(self):
            return (self.precio_compra + self.precio_venta) / 2
        
        def edit_compra_diaria(self,nueva_compra):
            self.compra_diaria=nueva_compra
        return (f"compra diaria actualizada a  {self.compra_diaria}.")

        def edit_venta_diaria(self,nueva_venta):
            self.venta_diaria = nueva_venta
        return(f"venta diaria actualizada a  {self.venta_diaria}")
        
        def edit_apertura(self,nueva_apertura):
            self.apertura = nuevo_apertura
        return ("f Minimo diario actualizado a  {self.apertura}")
    
        def edit_min_diario(self,nuevo_min):
            self.min_diario = nuevo_min
        return ("f Minimo diario actualizado a  {self.min_diario}")
        
        def edit_max_diario(self,nuevo_max):
            self.max_diario = nuevo_max
        return (f"Maximo diario actualizado a  {self.max_diario}")
        
        def ultimo_cierre(self,nuevo_cierre):
            self.ultimo_cierre = nuevo_cierre
        return (f" ultimo cierre actualizado a {self.ultimo_cierre}")
    
        def __str__(self):
            return (f " accion: {self.nombre_empresa} - ID:{self.id_accion} - ultimo cierre: {self.ultimo_cierre}")
    
    if __name__ == "__main__":
    
    #def alta_accion
    #def baja_accion
    #def edit_compra_diaria
    #def edit_venta_diaria
    #def edit_apertura
    #def edit_min_diario
    #def edit_max_diario
    #def edit_ultimo_cierre