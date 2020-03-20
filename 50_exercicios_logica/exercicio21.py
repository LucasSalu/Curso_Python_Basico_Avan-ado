matriz= []
quad = 5
for c in range(0,quad):
    matriz.append([10,10,10,10,10])

for c in range(0,quad):
    for b in range(0,quad):
        if c == b :
            matriz[c][b]=1
        else :
            matriz[c][b] = 0

for c in range(0,quad):
    for b in range(0,quad):
        print(matriz[c][b], end=" ")
    print('')
