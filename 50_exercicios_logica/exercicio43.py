'''conta quantidade de primos no intervalo do num'''
def primo(num):
    x = 0
    for c in range(1,num):
        if num % c == 0 and c != 1:
            x += 1
        elif num - 1 == c and x == 0 and c != 1:
            print(f'é primo {num}')


for c in range(100):
    primo(c)
