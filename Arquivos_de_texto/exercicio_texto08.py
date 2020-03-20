'''crie um programa que o usuario esccreva o nome do arquivo e passe todos os dados de um primeiro arquivo maiusculo'''
with open("arq.txt",'a+') as arquivo:
    with open(f"{str(input('digite o nome do arquivo'))}.txt", 'a+') as arquivo2:
        arquivo.seek(0)
        lista = arquivo.read()
        arquivo2.write(lista.upper())

