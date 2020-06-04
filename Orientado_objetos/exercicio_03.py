"""Cria uma agenda de pessoas podendo adicionar , remover e buscar """

class Pessoas:
    contador = 0
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def dados(self):
        return[self.__nome,self.__idade,self.__altura]

class Agenda:
    pessoa = []

    @classmethod
    def Armazena_pessoa(cls, nome, altura, idade):
        if len(cls.pessoa) < 10:
            cls.pessoa.append(Pessoas(nome,altura,idade))

    @classmethod
    def Remove_pessoa(cls, pessoa):
        for b,c in enumerate(cls.pessoa):
            if pessoa in c.dados()[0]:
                cls.pessoa.pop(b)
                print('pessoa removida com sucesso')

    @classmethod
    def Busca_pessoa(cls,pessoa):
        for b,c in enumerate(cls.pessoa):
            if c.dados()[0] in pessoa:
                print(b)

    @classmethod
    def Imprime_agenda(cls):
        for b,c in enumerate(cls.pessoa):
            print(f'{c.dados()[0]}',end=' ')
            print(f'{c.dados()[1]}m',end=' ')
            print(f'{c.dados()[2]} anos')


    @classmethod
    def Imprime_pessoa(cls, posicao):
        print('\n',cls.pessoa[posicao].dados()[0],end=' ')
        print(cls.pessoa[posicao].dados()[1],end=' ')
        print(cls.pessoa[posicao].dados()[2],end=' ')


agenda = Agenda # CRIA A AGENDA

agenda.Armazena_pessoa('lucas',1.80,20)     #ADICIONA PESSOA
agenda.Armazena_pessoa('bruno',1.70,18)     #ADICIONA PESSOA
agenda.Armazena_pessoa('kaike',1.60,18)     #ADICIONA PESSOA
agenda.Armazena_pessoa('vanessa',1.75,18)   #ADICIONA PESSOA
agenda.Armazena_pessoa('beatriz',1.16,18)   #ADICIONA PESSOA
agenda.Armazena_pessoa('fernanda',1.90,19)  #ADICIONA PESSOA

agenda.Remove_pessoa('lucas') #REMOVE PESSOA
agenda.Remove_pessoa('kaike') #REMOVA PESSOA

Agenda.Busca_pessoa('fernanda')#RETORNA A POSIÇAO
agenda.Busca_pessoa('beatriz')#RETORNA A POSIÇAO


agenda.Imprime_agenda()#IMPRIME AGENDA
agenda.Imprime_pessoa(1)






