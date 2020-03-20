vetor = [1,2,3,4,5,-1,-2,-3,-4,5]
for indice,variavel in enumerate(vetor):
    if variavel < 0:
        vetor[indice]=0
print(vetor)
