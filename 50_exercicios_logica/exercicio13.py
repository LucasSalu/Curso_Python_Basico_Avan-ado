notas = []

for c in range(0, 10):
    notas.append(float(input("Digite um numero")))
menor = min(notas)
maior = max (notas)

print(f"maior nota: {maior} nos indices :",end=' ')
for indice, variavel in enumerate(notas):
    if variavel == maior:
        print(f"{indice}",end=" - ")

print('')
print(f"menor nota: {menor} nos indices :", end=" ")
for indice, variavel in enumerate(notas):
    if variavel == menor:
        print(f"{indice}", end=" - ")
