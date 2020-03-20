''' encontra no arquivo quantas vezes aparece o texto digitado '''

from collections import Counter
with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    lista = arquivo.read()
    print(lista.count(str(input('digite um cactere'))))