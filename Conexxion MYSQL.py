import mysql.connector
from mysql.connector import errorcode

def conectar_mysql():
    try:
        return mysql.connector.connect(
            user="root",
            password="Mysql2024",
            host="localhost",
            database="ARGBrokerDemo",
            port="3306"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise "Usuario o Password no valido"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise "La Base de Datos no existe"
        else:
            raise err
    return None