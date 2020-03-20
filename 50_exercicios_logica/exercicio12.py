notas = []
z = 0
for c in range(0, 11):
    notas.append(float(input("Digite um numero")))
print(f" maior nota{max(notas)}")
print(f'menor nota {min(notas)}')
print(f"{sum(notas)/len(notas)}")
