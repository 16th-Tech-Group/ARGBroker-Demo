from Conexion_MySQL import conectar_mysql
#Crear Clase Inversor
class Inversor():
    def __init__(self,id_persona_cuit,id_billetera,nombre,id_perfil,id_localidad,ex_politica,calle,numero_calle,
                 correo_electronico,contraseña):
        self.__id_persona_cuit=id_persona_cuit
        self.__id_billetera=id_billetera
        self.__nombre=nombre
        self.__id_perfil = id_perfil
        self.__id_localidad=id_localidad
        self.__ex_politica=ex_politica
        self.__calle=calle
        self.__numero_calle=numero_calle
        self.__correo_electronico=correo_electronico
        self.__contraseña=contraseña
#Getters y Setters
    def get_id_persona_cuit(self):
        return self.__id_persona_cuit
    def Set_id_persona_cuit(self,id_persona_cuit):
        self.__id_persona_cuit = id_persona_cuit
    
    def get_id_billetera(self):
        return self.__id_billetera
    def Set_id_billetera(self,id_billetera):
        self.__id_billetera = id_billetera
        
    def get_nombre(self):
        return self.__nombre
    def Set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_id_perfil(self):
        return self.__id_perfil
    def Set_id_perfil(self,id_perfil):
        self.__id_perfil = id_perfil
    
    def get_id_localidad(self):
        return self.__id_localidad
    def Set_id_localidad(self,id_localidad):
        self.__id_localidad = id_localidad
    
    def get_ex_politica(self):
        return self.__ex_politica
    def Set_ex_politica(self,ex_politica):
        self.__ex_politica = ex_politica
    
    def get_calle(self):
        return self.__calle
    def Set_calle(self,calle):
        self.__calle = calle
    
    def get_numero_calle(self):
        return self.__numero_calle
    def Set_numero_calle(self,numero_calle):
        self.__numero_calle = numero_calle
    
    def get_correo_electronico(self):
        return self.__correo_electronico
    def Set_correo_electronico(self,correo_electronico):
        self.__correo_electronico = correo_electronico
    
    def get_contraseña(self):
        return self.__contraseña
    def Set_contraseña(self,contraseña):
        self.__contraseña = contraseña
          
#Creacion del Login de Usuario
    def loguin_usuario(self,correo_electronico,contraseña):
        try:
            if isinstance(correo_electronico, str) and contraseña != None: 
                usuarioL = conectar_mysql(Orden = f"Select correo_electronico from Inversores where correo_electronico = '{correo_electronico}';")
                contraseñaL = conectar_mysql(Orden = f"Select contraseña from Inversores where contraseña = '{contraseña}';")
                #La aplicacion del str sobre contraseña es realizada para evitar error en comparacion con numeros enteros
                #Sobre todo por que python con su tipado dinamico detecta a las contraseñas numericas como enteros y la base de datos retorna como cadena
                if usuarioL[0][0] == correo_electronico and contraseñaL[0][0] == str(contraseña):
                    return "Bienvenido"
                else:
                    return "El usuario Ingresado no existe"
            
            else:
                return ("El correo o la Contraseña estan mal escritos")
        except:
            raise ValueError ("Ocurrio un error")
         
#Alta Inversor
    def alta_inversor(self,id_persona_cuit,id_billetera,nombre,id_perfil,id_localidad,ex_politica,calle,numero_calle,
                 correo_electronico,contraseña):
        try:
            # Verificar si el inversor ya existe en la base de datos
            resultado = conectar_mysql(Orden=f"SELECT id_inversor FROM inversores WHERE id_inversor = '{id_persona_cuit}';")
            if resultado[0][0] == id_persona_cuit:  # Si el inversor ya existe
                return "Cuil ya registrado"
            else:
                # Si no existe, proceder a la inserción
                conectar_mysql(Orden = "INSERT INTO inversores (id_inversor,id_perfil,id_localidad,id_billetera,nombre,ex_plitica,calle,numero_calle,correo_electronico,contraseña) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                                Valores = [id_persona_cuit,id_billetera,nombre,id_perfil,id_localidad,ex_politica,calle,numero_calle,correo_electronico,contraseña])
                return "Inversor dado de alta exitosamente."
        except:
            return "Ocurrió un error al intentar dar de alta el inversor"

 # Baja Inversor
    def baja_inversor(self,id_persona_cuit,contraseña):
        try:
            resultado = conectar_mysql(Orden=f"SELECT id_inversor FROM inversores WHERE id_inversor = '{id_persona_cuit}'")
            PasswordL = conectar_mysql(Orden=f"SELECT contraseña FROM inversores WHERE contraseña = '{contraseña}'")
            
            if resultado[0][0] != id_persona_cuit: 
                return "El usuario no existe"
            else:
                if PasswordL[0][0] == str(contraseña): 
                    conectar_mysql(Orden=f"DELETE FROM inversores WHERE id_inversor = '{id_persona_cuit}';")
                    return "Inversor fue eliminado exitosamente."
                else:
                    return("La contraseña es incorrecta")
        except:
            return "Ocurrió un error al intentar eliminar el inversor"

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