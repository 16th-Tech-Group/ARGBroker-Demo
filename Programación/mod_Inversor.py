from Conexion_MySQL import conectar_mysql
from mod_Billetera import Billetera

#Crear Clase Inversor
class Inversor():
    def __init__(self,id_persona_cuit,id_billetera,nombre,id_localidad,ex_politica,calle,numero_calle,
                 correo_electronico,contraseña):
        self.__id_persona_cuit=id_persona_cuit
        self.__id_billetera=id_billetera
        self.__nombre=nombre
        self.__id_localidad=id_localidad
        self.__ex_politica=ex_politica
        self.__calle=calle
        self.__numero_calle=numero_calle
        self.__correo_electronico=correo_electronico
        self.__contraseña=contraseña

    def inversor_existe(self):
        """Verifica si un inversor existe en la base de datos basado en el id_persona_cuit"""
        try:
            query = "SELECT COUNT(*) FROM inversores WHERE id_persona_cuit = %s"
            valores = ({self.get_id_persona_cuit()})
            resultado = conectar_mysql(Orden=query, valores=valores)

        # Verifica si el resultado muestra al menos un registro
            return resultado[0][0] > 0 if resultado else False
        except Exception as e:
            return f"Error al verificar la existencia del inversor: {str(e)}"
         
#Creacion del Login de Usuario
    def loguin_usuario(self,correo_electronico,contraseña):
        try:
            correo_electronico=correo_electronico
            contraseña=contraseña
            if isinstance(correo_electronico, str) and contraseña != None: 
                usuarioL = conectar_mysql(Orden ="Select correo_electronico from Inversores where correo_electronico = ('{0}')".format(correo_electronico))
                contraseñaL = conectar_mysql(Orden ="Select contraseña from Inversores where correo_electronico = ('{0}')".format(correo_electronico))
                #La aplicacion del str sobre contraseña es realizada para evitar error en comparacion con numeros enteros
                #Sobre todo por que python con su tipado dinamico detecta a las contraseñas numericas como enteros y la base de datos retorna como cadena
                if usuarioL[0][0] == correo_electronico and contraseñaL[0][0] == str(contraseña):
                    print(correo_electronico + ",    Bienvenido a ARG BROKER DEMO")
                else:
                    print("El usuarion no existe, vuelva a ingresar")         
            else:
                print ("Error en alguna de las credenciales")
        except:
            raise ValueError ("Ocurrio un error")
         
#Alta Inversor
    def alta_inversor(self):
        try:
            id_persona_cuit=input("Cuit: ")
            # Verificar si el inversor ya existe en la base de datos
            resultado = conectar_mysql(Orden="SELECT COUNT(*) FROM inversores WHERE id_persona_cuit=('{0}')".format(id_persona_cuit))
            print(resultado[0][0])
            resultado=int(resultado[0][0])
            if resultado == 1:  # Si el inversor ya existe
                print("Cuil ya registrado")
                print("Volver a Ejecutar Menu Inicio")
            
            # Si no existe, proceder a la inserción
            else:
                id_persona_cuit=id_persona_cuit   
                nombre=input("Nombre: ")
                id_localidad=input("Localidad:")
                id_localidad=conectar_mysql("SELECT id_localidad FROM Localidades WHERE nombre_localidad=('{0}')".format(id_localidad))
                id_localidad=id_localidad[0][0]
                ex_politica=input("¿Es ud una Persona Expuesta Politicamente: ")
                calle=input("Calle: ")
                numero_calle=input("N°: ")
                correo_electronico=input("Usuario (Ingrese Correo Electronico: ")
                contraseña=input("Ingrese una contraseña: ")                     
                orden = """INSERT INTO inversores (id_persona_cuit, nombre, id_localidad, ex_politica, calle, numero_calle, correo_electronico, contraseña) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
                valores = (id_persona_cuit, nombre, id_localidad, ex_politica, calle, numero_calle, correo_electronico, contraseña)
                conectar_mysql(orden, valores)
        except Exception as e:
            return f"Ocurrió un error al intentar dar de alta el inversor: {str(e)}"

 # Baja Inversor
    def baja_inversor(self):
        if not self.inversor_existe():
            return "El inversor no existe en la base de datos."
        try:
            query = "DELETE FROM inversores WHERE id_persona_cuit = %s"
            valores = (self.get_id_persona_cuit(),)
            conectar_mysql(Orden=query, valores=valores)
            return "Inversor eliminado exitosamente."
        except Exception as e:
         return f"Ocurrió un error al intentar eliminar el inversor: {str(e)}"

# Editar Inversor
    def editar_inversor(self, **kwargs):
        if not self.inversor_existe():
            return "El inversor no existe en la base de datos."
    
        try:
            query = "UPDATE inversores SET "
            query += ", ".join([f"{key} = %s" for key in kwargs.keys()])
            query += " WHERE id_persona_cuit = %s"
        
            valores = list(kwargs.values()) + [self.get_id_persona_cuit()]
            conectar_mysql(Orden=query, valores=valores)
            return "Inversor actualizado exitosamente."
    
        except Exception as e:
            return f"Ocurrió un error al intentar actualizar el inversor: {str(e)}"

#Getters y Setters
    def get_id_persona_cuit(self):
        return self.__id_persona_cuit
    def set_id_persona_cuit(self,id_persona_cuit):
        self.__id_persona_cuit = id_persona_cuit
    def get_id_billetera(self):
        return self.__id_billetera
    def set_id_billetera(self,id_billetera):
        self.__id_billetera = id_billetera
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_id_localidad(self):
        return self.__id_localidad
    def set_id_localidad(self,id_localidad):
        self.__id_localidad = id_localidad
    
    def get_ex_politica(self):
        return self.__ex_politica
    def set_ex_politica(self,ex_politica):
        self.__ex_politica = ex_politica
    
    def get_calle(self):
        return self.__calle
    def set_calle(self,calle):
        self.__calle = calle
    
    def get_numero_calle(self):
        return self.__numero_calle
    def set_numero_calle(self,numero_calle):
        self.__numero_calle = numero_calle
    
    def get_correo_electronico(self):
        return self.__correo_electronico
    def set_correo_electronico(self,correo_electronico):
        self.__correo_electronico = correo_electronico
    
    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self,contraseña):
        self.__contraseña = contraseña

    def imprimir_datos(self):
        print(self.get_id_persona_cuit())