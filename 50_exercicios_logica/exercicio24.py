n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
    matriz.append([int(input()),int(input()), int(input()), int(input())])
for c in range(m):
    for d in range(m):
        if matriz[c][d] == m:
            print(f'{c} {d}')
        n = 1
if n != 1 :
    print("nao encontrado")



