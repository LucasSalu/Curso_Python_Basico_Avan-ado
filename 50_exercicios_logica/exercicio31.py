from random import randint
matriz = []
soma = 0
for c in range(0,5):
    matriz.append([randint(0,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(0,5),randint(1,5),randint(0,5),randint(1,5)])
for c in matriz:
    print(c)
for c in range(0,5):
    soma = 0
    for d in range(0,10):
        if   d == 0:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 1:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 2:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 3:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 4:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 5:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 6:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 7:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 8:
            if matriz[c][d] == 5:
                soma+=1
        elif d == 9:
            if matriz[c][d] == 5:
                soma+=1
    if soma >=7:
            print(f"aluno {c} aprovado com {soma}")
    else:
            print(f"aluno {c} reprovado com {soma}")

