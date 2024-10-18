import mod_Billetera
import mod_Accion
import mod_Tablas_Grales
import mod_Inversor
import mod_Operacion
import pytest

def test_verificar_usuario():
    User = Usuario(0,0)
    assert User.contraseña()
    