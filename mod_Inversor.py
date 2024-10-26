from Conexion_MySQL import conectar_mysql
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

#Creacion del Login de Usuario
    def verificar_usuario(self,correo_electronico,contraseña):
        while True:
            print("Ingrese su Correo y Contraseña:")
            correo_electronico = input("Ingrese su Correo:")
            contraseña = input("Ingrese su contraseña:")
            
            with conectar_mysql.cursor() as cursor:
                consulta =("select Inversores,pass from correo_electronico where correo_electronico=? and pass=?")
                cursor.execute(consulta,(correo_electronico,contraseña))
                
                resultado = cursor.fetchall()
                
            if resultado:
                for i in resultado:
                    return "Bienvenido"+i[0]
                break
            else:
                raise ValueError ("El Correo o la Contraseña es incorrecta")

#Crear Metodos
    #def alta()
    #def baja()
    #def editar()
    #def comprar() falta este
    #def vender() falta este
    #def depositar()
    #def retirar()
    #def consulta_billetera()