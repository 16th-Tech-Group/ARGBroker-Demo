from Conexion_MySQL import conectar_mysql
#Crear Clase Inversor
class Inversor():
    def __init__(self,id_persona_cuit,id_billetera,nombre,id_localidad,ex_politica,id_inversor,calle,numero_calle,
                 correo_electronico,contraseña):
        self.__id_persona_cuit=id_persona_cuit
        self.__id_billetera=id_billetera
        self.__nombre=nombre
        self.__id_localidad=id_localidad
        self.__ex_politica=ex_politica
        self.__id_inversor=id_inversor
        self.__calle=calle
        self.__numero_calle=numero_calle
        self.__correo_electronico=correo_electronico
        self.__contraseña=contraseña
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
    
    def get_id_inversor(self):
        return self.__id_inversor
    def set_id_inversor(self,id_inversor):
        self.__id_inversor = id_inversor
    
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

    def inversor_existe(self):
        """Verifica si un inversor existe en la base de datos basado en el id_persona_cuit"""
        try:
            query = "SELECT COUNT(*) FROM inversores WHERE id_persona_cuit = %s"
            valores = (self.get_id_persona_cuit(),)
            resultado = conectar_mysql(Orden=query, valores=valores)

        # Verifica si el resultado muestra al menos un registro
            return resultado[0][0] > 0 if resultado else False
        except Exception as e:
            return f"Error al verificar la existencia del inversor: {str(e)}"
         
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
                    return "El usuarion no existe"
            
            else:
                return ("El correo o la Contraseña estan mal escritos")
        except:
            raise ValueError ("Ocurrio un error")
         
# Alta Inversor
    def alta_inversor(self, id_persona_cuit, id_billetera, nombre, 
                    id_localidad, ex_politica, id_inversor, calle, 
                    numero_calle, correo_electronico, contraseña):
        try:
            # Verificar si el inversor ya existe en la base de datos
            resultado = conectar_mysql(Orden=f"SELECT id_persona_cuit FROM inversores WHERE id_persona_cuit='{id_persona_cuit}'")
            
            if resultado and resultado[0][0] == id_persona_cuit:  # Si el inversor ya existe
                return "Cuit ya registrado"
            else:
                Orden = """INSERT INTO inversores (id_persona_cuit, id_billetera, nombre, 
                    id_localidad, ex_politica, id_inversor, calle, numero_calle, correo_electronico, contraseña)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                Valores = [id_persona_cuit, id_billetera, nombre, 
                        id_localidad, ex_politica, id_inversor, 
                        calle, numero_calle, correo_electronico, contraseña]
                
                conectar_mysql(Orden=Orden, valores=Valores)
                return "Inversor dado de alta exitosamente."
        
        except Exception as e:
            return f"Ocurrió un error al intentar dar de alta el inversor: {str(e)}"


 # Baja Inversor
    def baja_inversor(self, id_persona_cuit):
        if not self.inversor_existe(id_persona_cuit):
            return "El inversor no existe en la base de datos."
        try:
            query = "DELETE FROM inversores WHERE id_persona_cuit = %s"
            valores = (id_persona_cuit,)
            conectar_mysql(Orden=query, valores=valores)
            return "Inversor eliminado exitosamente."
        except Exception as e:
            return f"Ocurrió un error al intentar eliminar el inversor: {str(e)}"


    # Editar Inversor
    def editar_inversor(self, id_persona_cuit, id_billetera=None, nombre=None, id_localidad=None, 
                        ex_politica=None, id_inversor=None, calle=None, numero_calle=None, 
                        correo_electronico=None, contraseña=None):
        
        if not self.inversor_existe(id_persona_cuit):
            return "El inversor no existe en la base de datos."

        # Filtra los parámetros que no son None y genera la lista de campos a actualizar
        campos_a_actualizar = { 
            "id_billetera": id_billetera, 
            "nombre": nombre, 
            "id_localidad": id_localidad, 
            "ex_politica": ex_politica, 
            "id_inversor": id_inversor, 
            "calle": calle, 
            "numero_calle": numero_calle, 
            "correo_electronico": correo_electronico, 
            "contraseña": contraseña
        }
        campos_a_actualizar = {key: value for key, value in campos_a_actualizar.items() if value is not None}
        
        if not campos_a_actualizar:
            return "No se proporcionaron campos para actualizar."

        try:
            query = "UPDATE inversores SET "
            query += ", ".join([f"{key} = %s" for key in campos_a_actualizar.keys()])
            query += " WHERE id_persona_cuit = %s"
            
            valores = list(campos_a_actualizar.values()) + [id_persona_cuit]
            conectar_mysql(Orden=query, valores=valores)
            return "Inversor actualizado exitosamente."
        
        except Exception as e:
            return f"Ocurrió un error al intentar actualizar el inversor: {str(e)}"
