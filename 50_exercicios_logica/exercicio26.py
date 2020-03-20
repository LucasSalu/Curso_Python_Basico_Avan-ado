matriz = []
for c in range(0,10):
    matriz.append([0]*10)
for c in range(0,10):
    for d in range(0,10):
        if c < d:
            matriz[c][d]=(2*c)+(7*d)-2
        elif c == d:
            matriz[c][d] = 3*(c*c) - 1
        elif c > d:
            matriz[c][d] = 4*(c*c*c)-5*(d*d)

for c in matriz:
    print(c)
