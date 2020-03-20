"""crie um vetor dee 8 elementos e some duas posiçoes escolhidas pelo usiario"""
vetor1 = []
for a in range(0,8):
    vetor1.append(int(input('Diigte um valor: ')))
x = int(input('Diigte o valor de "x": '))
y = int(input('Diigte o valor de "y": '))
print(f'{vetor1[x]+vetor1[y]}')
