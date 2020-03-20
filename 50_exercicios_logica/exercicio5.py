'''contar numeros pares no verto '''
x = 0
vetor1 = []
for c in range(0,10):
    vetor1.append(int(input('Diigte um valor: ')))
for c in vetor1:
    if c%2 == 0:
        x+=1
print(f"o vetor possui {x} numeros pares ")
