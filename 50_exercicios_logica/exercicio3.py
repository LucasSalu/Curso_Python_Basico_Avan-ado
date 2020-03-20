"""'Crie um conjunto com 10 elementos e outro com os quadrados dos elementos de entrada"""
conjunto_1 = []
conjunto_2 = []
for a in range(0,10):
    conjunto_1.append(float(input('digite um valor')))
    conjunto_2.append(conjunto_1[a]**2)
print(conjunto_1)
print(conjunto_2)




