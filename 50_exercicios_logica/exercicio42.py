'''calcula o fatorial de um numero'''
def fatorial(fatorial):
    soma = 1
    for c in range(fatorial,0,-1):
        print(c)
        soma *= c
    return soma
print(fatorial(5))
