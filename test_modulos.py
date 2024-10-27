from mod_Billetera import Billetera
from mod_Accion import Accion
#from mod_Tablas_Grales
from mod_Inversor import Inversor
#from mod_Operacion
import pytest

def test_loguin_usuario():
    usuario_1 = Inversor(1,29034678,"Raul",4,0,16,"Alabama",3028,"raul45@gmail.com",123456)
    assert usuario_1.loguin_usuario("raul45@gmail.com",123456) == "Bienvenido"
    
    

    