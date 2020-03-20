notas = []
x = 0
y = 0
z = 0
for c in range(0, 10):
    notas.append(float(input("Digite um numero")))
    if notas[c] < 0:
        x += 1
print(f"numeros negativos {x}\nnumeros positivos {len(notas)- x}")





