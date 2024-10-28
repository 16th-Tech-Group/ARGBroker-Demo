#Crear Clase Inversor
class Inversor():
    def __init__(self,id_persona_cuit,id_billetera,nombre,id_localidad,ex_politica,id_inversor,calle,numero_calle,
                 correo_electronico,contraseña):
        self.id_persona_cuit=id_persona_cuit
        self.id_billetera=id_billetera
        self.nombre=nombre
        self.id_localidad=id_localidad
        self.ex_politica=ex_politica
        self.id_inversor=id_inversor
        self.calle=calle
        self.numero_calle=numero_calle
        self.correo_electronico=correo_electronico
        self.contraseña=contraseña
class Inversor:
    def __init__(self):
        self.inversores = {}
#Creacion del Loguin de Usuario
    def verificar_usuario(self,correo_electronico,contraseña):
        if correo_electronico == "1234" and contraseña == 1234:
            return "exit"
        else:
            raise ValueError ("El Correo o la Contraseña son incorrectos ")

    def alta(self, nombre, datos):
        """Añadir un nuevo inversor."""
        if nombre in self.inversores:
            print(f"El inversor {nombre} ya existe.")
        else:
            self.inversores[nombre] = {
                "datos": datos,
                "billetera": 0.0
            }
            print(f"Inversor {nombre} creado con éxito.")

    def baja(self, nombre):
        """Eliminar un inversor."""
        if nombre in self.inversores:
            del self.inversores[nombre]
            print(f"Inversor {nombre} eliminado con éxito.")
        else:
            print(f"El inversor {nombre} no existe.")

    def editar(self, nombre, nuevos_datos):
        """Editar un inversor existente."""
        if nombre in self.inversores:
            self.inversores[nombre]["datos"] = nuevos_datos
            print(f"Inversor {nombre} editado con éxito.")
        else:
            print(f"El inversor {nombre} no existe.")

    def depositar(self, nombre, monto):
        """Depositar dinero en la billetera del inversor."""
        if nombre in self.inversores:
            self.inversores[nombre]["billetera"] += monto
            print(f"Se han depositado ${monto} en la billetera de {nombre}.")
        else:
            print(f"El inversor {nombre} no existe.")

    def retirar(self, nombre, monto):
        """Retirar dinero de la billetera del inversor."""
        if nombre in self.inversores:
            if self.inversores[nombre]["billetera"] >= monto:
                self.inversores[nombre]["billetera"] -= monto
                print(f"Se han retirado ${monto} de la billetera de {nombre}.")
            else:
                print(f"Saldo insuficiente en la billetera de {nombre}.")
        else:
            print(f"El inversor {nombre} no existe.")

    def consultar_billetera(self, nombre):
        """Consultar el saldo de la billetera del inversor."""
        if nombre in self.inversores:
            saldo = self.inversores[nombre]["billetera"]
            print(f"El saldo de la billetera de {nombre} es: ${saldo}.")
        else:
            print(f"El inversor {nombre} no existe.")

    def mostrar_inversores(self):
        """Mostrar todos los inversores."""
        if not self.inversores:
            print("No hay inversores disponibles.")
        else:C
            for nombre, info in self.inversores.items():
                print(f"Inversor: {nombre}, Datos: {info['datos']}, Billetera: ${info['billetera']}")

Usuario = Inversor(0,0)

#Crear Metodos
    #def alta()
    #def baja()
    #def editar()
    #def comprar() falta este
    #def vender() falta este
    #def depositar()
    #def retirar()
    #def consulta_billetera()