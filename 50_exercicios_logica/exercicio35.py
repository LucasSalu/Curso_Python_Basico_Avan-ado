def descobre_quadrado(num):

    '''informa se um num é u quadrado perfeito '''

    for c in range(num):
        if c*c == num:
            print(f'é o quadrado perfeito de {c}')
            return c