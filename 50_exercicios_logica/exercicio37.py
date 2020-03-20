'''converte horas minutos em segundos totais
'''
def contverte_segundos(horas, minutos, segundos):
    horas = horas*60*60
    minutos *= 60
    return horas+minutos+segundos
print(contverte_segundos(int(input()),int(input()),int(input())))
