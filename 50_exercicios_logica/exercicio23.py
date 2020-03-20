matriz= []
for c in range(0,4):
    matriz.append([int(input()),int(input()),int(input()),int(input())])

x = 0
y = 0

for c in range(0,4):
    for b in range(0,4):
        if c == 0 and b == 0:
            x = c
            y = b
        elif matriz[c][b]>matriz[x][y]:
            x = c
            y = b
print(matriz[x][y])

for c in range(0,4):
    for b in range(0,4):
        print(matriz[c][b], end=" ")
    print('')


