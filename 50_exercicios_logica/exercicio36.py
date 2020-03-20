from math import pi
def volume_esfera(raio):
    '''calcula o volume de uma esfera'''
    return ((4/3)*pi)*(raio**3)


print(volume_esfera(float(input('digite o raio'))))