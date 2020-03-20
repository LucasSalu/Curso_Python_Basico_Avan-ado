'''Desenha um triangulo lateral'''
def triangulo(num):
    x = num*2-1
    print(x)
    for c in range(0,x):
        if c <= num:
            print("*"*c)
    for c in range(x,0,-1):
        if c < num:
            print("*" *c)

triangulo(20)