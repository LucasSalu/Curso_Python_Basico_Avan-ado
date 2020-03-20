'''informa o volume de um cilindro'''
from math import pi
def volume_cilindro(altura,raio):
    return((raio**2)*pi)*altura


print(volume_cilindro(int(input()),int(input())))