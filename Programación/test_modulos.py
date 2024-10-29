from mod_Billetera import Billetera
from mod_Accion import Accion
#from mod_Tablas_Grales
from mod_Inversor import Inversor
#from mod_Operacion
import pytest

#Test Modulo Accion

#Test Modulo Billetera

#Test Modulo Inversor

def test_loguin_usuario():
    user_1 = Inversor(2,1,"Juan Perez",0,1,"NO","Calle Falsa",123,"juan.perez@example.com",1234)
    assert user_1.loguin_usuario("juan.perez@example.com",1234) == "Bienvenido"
    
def test_alta_inversor():
    user_1 = Inversor(2,1,"Juan Perez",0,1,"NO","Calle Falsa",123,"juan.perez@example.com",123)
    assert user_1.alta_inversor(2,1,"Juan Perez",0,1,"NO","Calle Falsa",123,"juan.perez@example.com",1234) == "Cuil ya registrado"

def test_baja_inversor():
    user_1 = Inversor(2,1,"Juan Perez",0,1,"NO","Calle Falsa",123,"juan.perez@example.com",1234)
    assert user_1.baja_inversor(2,1234) == "Inversor fue eliminado exitosamente."
    
#Test Modulo Operacion

#Test Modulo Tablas Generales