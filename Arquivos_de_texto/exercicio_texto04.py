'''conta quantas consoantes existem no arquivo'''
from collections import Counter


def conta_vogal(lista):
    return lista.count('a')+lista.count('e')+lista.count('i')+lista.count('o')+lista.count('u')


with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    arq = arquivo.read()
    print(f'consoantes ==> {-1*(conta_vogal(arq)+arq.count(" ")-len(arq))}')
    print(f'vogais ==== > {conta_vogal(arq)}')
