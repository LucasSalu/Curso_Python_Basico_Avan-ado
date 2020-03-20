vetor1 = []
x = 0
y = 0
while True:
    y = int(input())
    if y % 2 == 0:
        vetor1.append(y)
        x += 1
        if x == 6:
            x = 0
            break

for c in vetor1 :
    x += c
print(x / len(vetor1))
