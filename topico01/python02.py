class Veiculo:
    def __init__(self, ano_fabricacao, cor, marca):
        self._ano_de_fabricacao = ano_fabricacao
        self.cor = cor
        self.marca = marca

    def getAnoFabricacao(self):
        return self._ano_de_fabricacao

    def showAllProperties(self):
        pickAg = self.getAnoFabricacao();
        print(pickAg)
        print(self._ano_de_fabricacao)
        print(self.cor)
        print(self.marca)

class Carro(Veiculo):
    def __init__(self, ano_fabricacao, cor, marca, cor_xan):
        super().__init__(ano_fabricacao, cor, marca)
        self.corDaXana = cor_xan
    
    def showAllProperties(self):
        super().showAllProperties()
        print(self.corDaXana)

c1 = Carro(2023, "Azul", "Peugeot", "Vermelhinha")
c1.showAllProperties()