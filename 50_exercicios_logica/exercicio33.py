def data(dia, mes, ano):
    ''' entra com a data e escreve por extenso a o mes '''
    meses = {1: 'Janeiro', 2: 'Fevereiro,', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    if mes in meses:
        return f'{dia} de {meses[mes]} de {ano}'


print(data(int(input('digite o dia')),int(input('digite o mes')),int(input('digite o ano'))))

