import pytest
from src.dni_cif import Dni

@pytest.fixture(name="dni")
def inyector():
    return Dni()

def test_constructor_default(dni):
    assert dni.getDni() == ""
    assert not dni.getNumeroSano()
    assert not dni.getLetraSana()

def test_setters_getters(dni):
    dni.setDni("12345678Z")
    assert dni.getDni() == "12345678Z"