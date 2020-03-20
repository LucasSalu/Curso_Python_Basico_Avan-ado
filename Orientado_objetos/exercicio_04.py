'''Crie uma classe elevador que vc determine a quantidade de andares '''
class Elevador:
    andar = 0
    pessoas = 0
    def __init__(self,andares,capacidade):
        self.__andares = andares
        self.__capacidade = capacidade

    def Entra(self):
        if Elevador.pessoas + 1 > self.__capacidade:
            print("capacidade excedida")
        else:
            Elevador.pessoas += 1
            print(Elevador.pessoas)

    def Sai(cls):
        if cls.pessoas -1 < 0:
            print("Nao existe passageiro")
        else:
            Elevador.pessoas -= 1

    def Sobe(self):
        if Elevador.andar + 1 > self.__andares:
            print('você ja esta no ultimo andar')
        else:
            Elevador.andar += 1
    @classmethod
    def desce(cls):
        if cls.andar - 1 < 0:
            print('voce ja esta no terreo')
        else:
            Elevador.andar -= 1


lucas = Elevador(20,20)






