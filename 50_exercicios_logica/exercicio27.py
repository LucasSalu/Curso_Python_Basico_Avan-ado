from random import randint
matriz = []
soma = 0
for c in range(0,4):
    matriz.append([randint(0,20),randint(0,20),randint(0,20),randint(0,20)])
for c in range(0,4):
    for d in range(0,4):
        if d>c:
            soma += matriz[c][d]
for c in matriz:
    print(c)
print(soma)