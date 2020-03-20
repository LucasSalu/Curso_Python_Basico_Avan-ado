vetor = [1,2,3,4,5,-1,-2,-3,-4,5]
x= int(input('digite u numero inteiro'))
for c in vetor:
    if c%x == 0:
        print(c,end=" ")
print(".")