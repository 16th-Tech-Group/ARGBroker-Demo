from Conexion_MySQL import conexion
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
    def loguin_usuario(self,correo_electronico,contraseña):
        cursor = conexion.cursor()
        cursor.execute("select * from provincia;")
        provincia = cursor.fetchall()
        
        return provincia
        
    
    
