import random
matriz1=[]
matriz2=[]
matriz3=[]
for c in range(0,4):
    matriz1.append([random.randint(0,20)]*4)
    matriz2.append([random.randint(0, 20)] * 4)
    matriz3.append([0]*4)

print(matriz1,"\n",matriz2)
for c in range(0,4):
    for d in range(0,4):
        if matriz1[c][d] > matriz2[c][d]:
            matriz3[c][d] = matriz1[c][d]
        elif matriz1[c][d] < matriz2[c][d]:
            matriz3[c][d] = matriz2[c][d]
        else:
            matriz3[c][d] = matriz1[c][d]
print(matriz3)