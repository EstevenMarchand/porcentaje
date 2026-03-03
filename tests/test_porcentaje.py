import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from porcentaje import porcentaje

def test_porcentaje_caso_correcto():
    assert porcentaje(200, 10) == 999  # MAL a propósito

def test_porcentaje_caso_limite_cero_por_ciento():
    assert porcentaje(999, 0) == 0

def test_porcentaje_caso_error_cantidad_negativa():
    with pytest.raises(ValueError):
        porcentaje(-100, 10)

def test_porcentaje_caso_error_tipo_invalido():
    with pytest.raises(TypeError):
        porcentaje("100", 10)