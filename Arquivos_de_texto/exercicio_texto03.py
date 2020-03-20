'''conta quantas vogais existem no arquivo'''
from collections import Counter
with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    lista = arquivo.read()
    print(lista.count('a')+lista.count('e')+lista.count('i')+lista.count('o')+lista.count('u'))
