import mysql.connector
from mysql.connector import errorcode

# funcion de consulta y otros metodos

#   Consulta
# NombreUsuario =  Conectar_Mysql('select * from personas where cuil = 22222222')

# Insert 
#
# Conectar_mysql(Orden="insert into Personas (cuil, nombre, apellido) values (%s,%s,%s)", Valores=[22222,bauti,bustos])

def conectar_mysql(Orden, Valores = None):
    # orden y valores
    try:
        # conexion 
        Cnx = mysql.connector.connect(
                user="root",
                password="30060512V",
                host="localhost",
                database="ARGBrokerDemo",
                port="3306")
        
        # persona, cuil, nombre 
        #   orden = 'select * from Personas where cuil='{Variable}' '
        #   str (select * from eprsonas where cuil=2020020200)


        if Valores == None: #si no hay valores, es consulta
            Cursor = Cnx.cursor()
            Cursor.execute(Orden)
            # indicador de datos
            lista=[] #lista que guarda la consulta
            for i in Cursor.fetchall():
                lista.append(i) 
            return lista
        
        # Orden = 'insert in to personas(id_persona, cuit_persona, Nombre) Values(%s,%s,%s)'
        # Valores = [22, 20460361312, Bauti]
        else: 
            Cursor = Cnx.cursor()
            Cursor.execute(Orden,Valores)
            Cnx.commit()


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise "Usuario o Password no valido"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise "La Base de Datos no existe"
        else:
            raise err





if __name__ == '__main__':
    
    conectar_mysql(Orden = "insert into Provincias (id_provincia,nombre_provincia) Values(%s,%s)",
                   Valores = [3,"Cordoba"])

