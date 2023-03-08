"""
Primos de Rafael Echevarria
"""

def esPrimo(numero):
    """
    La funcion devuelve `True` si su argumento es primo, y `False` si no lo es.
    
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, numero):
        if numero % prueba == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([ prueba for prueba in range(2, numero) if esPrimo(prueba) ])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """
    factors = []
    
    while esPrimo(numero):
        factors.append(2)
        numero //= 2
    
    for f in primos(numero):
        while numero % f == 0:
            factors.append(f)
            numero //= f
    
    if numero > 2:
        factors.append(numero)
    
    return tuple(factors)

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    # Descomponer a y b en factores primos
    f_primos_1 = descompon(numero1)
    f_primos_2 = descompon(numero2)

    # Combinar factores primos comunes y no comunes
    f_primos = []
    for factor in f_primos_1:
        if factor in f_primos_2:
            f_primos_2.remove(factor)
        f_primos.append(factor)
    f_primos += f_primos_2

    # Calcular el producto de los factores primos
    mcm = 1
    for factor in f_primos:
        mcm *= factor

    return mcm

def mcd(numero1, numero2):
    f_primos_1 = descompon(numero1)
    f_primos_2 = descompon(numero2)
    interseccion = set(f_primos_1).intersection(f_primos_2)

    mcd = 1
    for factor in interseccion:
        mcd *= factor
    return mcd


import doctest

doctest.testmod()