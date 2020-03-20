matriz= []
quad = 4
for c in range(0,quad):
    matriz.append([10,10,10,10])

for c in range(0,quad):
    for b in range(0,quad):
            matriz[c][b]=(c*b)

for c in range(0,quad):
    for b in range(0,quad):
        print(matriz[c][b], end=" ")
    print('')
