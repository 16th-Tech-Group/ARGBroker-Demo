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
    
    def get_id_localidad(self):
        return self.__id_localidad
    def Set_id_localidad(self,id_localidad):
        self.__id_localidad = id_localidad
    
    def get_ex_politica(self):
        return self.__ex_politica
    def Set_ex_politica(self,ex_politica):
        self.__ex_politica = ex_politica
    
    def get_id_inversor(self):
        return self.__id_inversor
    def Set_id_inversor(self,id_inversor):
        self.__id_inversor = id_inversor
    
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
                    return "El usuarion no existe"
            
            else:
                return ("El correo o la Contraseña estan mal escritos")
        except:
            raise ValueError ("Ocurrio un error")
         
            
            
#Inversor.loguin_usuario("raul45@gmail.com","123456")
    
