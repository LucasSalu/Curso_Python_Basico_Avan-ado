'''ordena pelas musicas mais tocadas '''
usuarios = [{'titulo': 'Dias de lutas Dias de Gloria', 'tocou':1},
            {'titulo': 'Your say', 'tocou':5},
            {'titulo': 'Ousado amor', 'tocou':3},
            {'titulo': 'refugio no deserto', 'tocou':4},
            {'titulo': 'Deus de milagres', 'tocou':1}]


def add_musica():
    usuarios.append({'titulo':str(input(' digite o nome da musica\n')), 'tocou': int(input('digite o numero de vezes tocada\n'))})


add_musica()
add_musica()

for c in sorted(usuarios, key=lambda usuario: usuario['tocou'], reverse= True):
    for key,prod in c.items():
        if type(prod) == type(str()):
            print(prod.title())

