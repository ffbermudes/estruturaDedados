class ContaPoupanca:
    def __init__(self, nConta, correntista, saldoAtual):
        self.conta_poupanca = nConta
        self.usuario = correntista
        self.saldo = saldoAtual

    def showAllDataInAccount(self):
        print(self.usuario)
        print(self.saldo)
        print(self.conta_poupanca)
    
    def transferencia(self, value):
        if(not self.saldo < value):
            self.saldo -= value
            return True

        else: False

    def deposito(self, value):
        if(value > 0):
            self.saldo += value

class ContaCorrente(ContaPoupanca):

    def __init__(self, nConta, correntista, saldoAtual):
        super().__init__(nConta, correntista, saldoAtual)
        self.__taxa = 1

    def transferenciaComTaxa(self, value):
        aplicaTaxa = super().transferencia(value)
        if( not aplicaTaxa != False):
            self.saldo -= self.__taxa
            return self.saldo
        else:
            print('Você está pobre !')
            return self.saldo

c1 = ContaCorrente(666, "Joaquim", 5000)
print(c1.transferenciaComTaxa(3000))