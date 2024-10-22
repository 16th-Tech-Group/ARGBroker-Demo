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

#Declarar Metodos
    #def alta_accion
    #def baja_accion
    #def edit_compra_diaria
    #def edit_venta_diaria
    #def edit_apertura
    #def edit_min_diario
    #def edit_max_diario
    #def edit_ultimo_cierre


    def mostrar_max_diario(self):
        return(f"El monto máximo diario es: {self.max_diario}")
    
#def edit_max_diario
    def editar_max_diario(self,nvo_max_diario):
        self.max_diario=nvo_max_diario
        return(f"Monto mínimo diario actualizado a: {self.min_diario}")
    

    def mostrar_min_diario(self):
        return (f"El mínimo diario es: {self.min_diario}")
    
#def edit_min_diario
    def editar_min_diario(self,nvo_min_diario):
        self.min_diario=nvo_min_diario
        return(f"Monto mínimo diario actualizado a: {self.min_diario}")

#instancia max    
accion = Accion(1, "Empresa X", 100, 200, 150, 120, 130, 90, 160, 140)

print(accion.mostrar_min_diario())
print(accion.editar_min_diario(85))
print(accion.mostrar_min_diario())

''' #instancia min
accion = Accion(1, "Empresa X", 100, 200, 150, 120, 130, 90, 160, 140)

print(accion.mostrar_max_diario())
print(accion.editar_max_diario(133))
print(accion.mostrar_max_diario())''' 
