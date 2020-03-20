'''Desenha um triangulo'''
def triangulo(base):
    x = base*2-1
    y = 2
    for c in range(0,base):
        print(' '*base, end="")
        if c == 0:
            print('*' * (c + 1))
        else :
            print('*'*(c+y))
            y += 1
        base -= 1

triangulo(int(input('digite um numero de 1 a 100')))