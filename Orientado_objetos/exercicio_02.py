'''imprime as os atributos da classe pessoa'''

class Pessoas:
    contador = 0
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def dados(self):
        print(f'nome {self.__nome} idade {self.__altura} altura {self.__idade}')
