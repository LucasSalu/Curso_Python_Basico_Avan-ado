'''Classe que simula um a conta no banco que realiza transferencias podem consultar saldo'''
class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.limite = limite
        Conta.contador += 1


    def extrato(self):
        print(f'Saldo de {self.__saldo} do Titular {self.__titular} com limite de {self.limite}')

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self,valor,conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor



usuario = Conta('Lucas', -32, 1000)
usuario1 = Conta('vanice,',1000,10000)

usuario1.transferir(50,usuario)

usuario1.extrato()
usuario.extrato()

