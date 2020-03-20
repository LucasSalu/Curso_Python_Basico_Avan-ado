vetor = [10,20,30,40,50,60,70,80,90,90]

for indice,variavel in enumerate(vetor):
    for indice1,variavel1 in enumerate(vetor):
        if indice != indice1:
            if variavel == variavel1:
                print(variavel)

