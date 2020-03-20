
with open("arq.txt",'a+') as arquivo:
    arquivo.seek(0)
    print(f'o arquivo txt possui {len(arquivo.readlines())} linhas')
