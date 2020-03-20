vetor = []
for c in range(0,5):
    vetor.append(int(input("digite um valor")))
x = int(input("digite um valor"))

if x == 1:
    print(vetor[::1])
elif x == 2:
    print(vetor[::-1])
elif x != 0:
    print("codigo invalido")