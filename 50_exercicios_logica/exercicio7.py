vetor1 = [11,12,13,14,15,16,17,18,19,10]

for indice,variavel in enumerate(vetor1):
    for indice1,variavel1 in enumerate(vetor1):
        if indice != indice1:
            if variavel == variavel1:
                print({variavel1,})
