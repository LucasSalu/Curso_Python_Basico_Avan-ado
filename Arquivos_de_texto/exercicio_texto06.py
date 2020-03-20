'''mostra quantas vezes cada caracter aparece'''
from collections import Counter
with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    lista = Counter(arquivo.read())
    for c,a in lista.most_common(26):
        print(f"a letra '{c}' aparece '{a}'")