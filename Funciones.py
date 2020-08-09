import math


def suma_compleja(c1, c2):
    a = c1[0] + c2[0]
    b = c1[1] + c2[1]
    result = (a, b)
    return result


def multiplicacion_compleja(c1, c2):
    a = (c1[0]*c2[0]) - (c1[1]*c2[1])
    b = (c1[1]*c2[0]) + (c1[0]*c2[1])
    result = (a, b)
    return result


def sustracion_compleja(c1, c2):
    a = c1[0] - c2[0]
    b = c1[1] - c2[1]
    result = (a, b)
    return result


def division_compleja(c1, c2):
    a = ((c1[0]*c2[0]) + (c1[1]*c2[1]))/(c2[0]**2 + c2[1]**2)
    b = ((c2[0]*c1[1]) - (c1[0]*c2[1]))/(c2[0]**2 + c2[1]**2)
    result = (a,b)
    return result


def modulo(c):
    result = math.sqrt(c[0]**2 + c[1]**2)
    return result


def conjugado(c):
    result = (c[0], c[1]*-1)
    return result


def polar_a_carte(polar):
    x = polar[0]*math.cos(polar[1])
    y = polar[0]*math.sin(polar[1])
    result = (round(x, 4), round(y, 4))
    return result


def carte_a_polar(coords):
    p = math.sqrt(coords[0]**2+coords[1]**2)
    ang = fase_compleja(coords)
    result = (p, ang)
    return result


def fase_compleja(c):
    fase = math.atan(c[1]/c[0])
    if c[0] < 0 and c[1] < 0:
        result = 180 + math.degrees(fase)
    elif c[0] < 0:
        result = 180 + math.degrees(fase)
    elif c[1] < 0:
        result = 360 + math.degrees(fase)
    else:
        result = math.degrees(fase)
    return result
