"""
Módulo: porcentaje

Contiene una función para calcular un porcentaje de una cantidad.
"""

def porcentaje(cantidad, porcentaje):
    """
    Calcula el valor que representa 'porcentaje' % de 'cantidad'.

    Fórmula:
        resultado = cantidad * (porcentaje / 100)

    Parámetros:
        cantidad (int|float): número sobre el que se calcula el porcentaje.
        porcentaje (int|float): porcentaje a aplicar (puede ser 0, positivo o negativo).

    Retorna:
        float: el resultado del porcentaje aplicado a la cantidad.

    Excepciones:
        TypeError: si cantidad o porcentaje no son numéricos.
        ValueError: si cantidad es negativa.
    """
    # Validación de tipos
    if not isinstance(cantidad, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("cantidad y porcentaje deben ser números (int o float).")

    # Validación de reglas
    if cantidad < 0:
        raise ValueError("cantidad no puede ser negativa.")

    return cantidad * (porcentaje / 100)