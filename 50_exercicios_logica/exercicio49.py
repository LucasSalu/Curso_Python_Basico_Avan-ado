'''Digita a musica mais tocada MAX E MIN'''
usuarios = [{'titulo': 'Dias de lutas Dias de Gloria', 'tocou':1},
            {'titulo': 'Your say', 'tocou':5},
            {'titulo': 'Ousado amor', 'tocou':3},
            {'titulo': 'refugio no deserto', 'tocou':4},
            {'titulo': 'Deus de milagres', 'tocou':1}]

print(max(usuarios, key=lambda usuario: usuario['tocou']))
