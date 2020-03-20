'''entre com os textos para gravar em cada linha do arquivo arquivo'''
with open('texto.txt','a+') as arquivo:
    while True:
        text = input("digite uma palavra")
        if text != "0":
            arquivo.write(text+'\n')
        else:
            break
    arquivo.seek(0)
    print(arquivo.read())





