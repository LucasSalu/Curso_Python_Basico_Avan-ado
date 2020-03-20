''' Desenha exclamaçao'''

def esclamacao(num):
    for c in range(0,num):
        for d in range(0,num):
            if c >= d:
                print("!",end='')
        print()

esclamacao(5)
