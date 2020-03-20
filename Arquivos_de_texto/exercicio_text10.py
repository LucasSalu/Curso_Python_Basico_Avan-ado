'''le de um arquivo as cidades mais populosas e retorna a mais populosa'''
cidade = ''
populacao = 0

with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    lista = arquivo.read().split('\n')

    for c in lista:
        a = c.split('-').copy()
        if populacao < int(a[1].replace('.','')):
            populacao = int(a[1].replace('.',''))
            cidade = c.split('-')[0]
            print(int(a[1].replace('.','')))
    print(f'{cidade} é a cidade mais populosa com {populacao} de habitantes')


