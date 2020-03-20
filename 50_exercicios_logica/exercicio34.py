def negativo(num):
    '''funçao identifica numeros negativos positivos e se é igual a zero'''
    if num > 0:
        print("numero positivo")
        return 1
    elif num < 0:
        print('numero negativo')
        return -1
    else:
        print('numero =  0')
        return 0

negativo(int(input('digite um numero')))