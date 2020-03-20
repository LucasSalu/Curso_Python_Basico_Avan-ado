'''Faça um pragrama que leia o conteudo de dois arquivos seguidos em um terceiro'''
with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    arq = arquivo.read()
    with open("arq2.txt", 'a+') as arquivo2:
        arquivo2.seek(0)
        arq12 = arquivo2.read()
        with open("arq3.txt",'a+') as arquivo3:
            arquivo3.write(arq)
            arquivo3.write(arq12)
