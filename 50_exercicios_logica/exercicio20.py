matriz= []
for c in range(0,4):
    matriz.append([int(input()),int(input()),int(input()),int(input())])
print(matriz[0][0])
x = 0
for c in range(0,4):
    for b in range(0,4):
        if matriz[c][b]>10:
            x += 1
print(x)
