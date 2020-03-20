'''simplifica a fraçao'''
def simplifica(dividendo,divisor):
    if dividendo>divisor:
        for c in range(1,dividendo):
            if dividendo % c == 0 and divisor % c == 0:
                dividendo /= c
                divisor /= c
    else:
        if dividendo < divisor:
            for c in range(1, divisor):
                if dividendo % c == 0 and divisor % c == 0:
                    dividendo /= c
                    divisor /= c

    print(f'{dividendo}/{divisor}')
    return [divisor,dividendo]


simplifica(100,50)


