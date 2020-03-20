from random import randint
matriz = []
soma = 0
for c in range(0,4):
    matriz.append([randint(1,20),randint(1,20),randint(1,20),randint(1,20)])
for c in range(0,4):
    for d in range(0,4):
        if c+d ==3:
            matriz[c][d]=0
for c in matriz:
    print(c)