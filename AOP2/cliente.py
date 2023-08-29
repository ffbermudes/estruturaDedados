class Cliente():
	def __init__(self, nome:str, valorDaConta:float) -> None:
		self.nome = nome
		self.valorDaConta = valorDaConta

	def __repr__(self) -> str:
		return f"{self.nome} - {self.valorDaConta}"

# teste = Cliente("Filipe", 30)
# print(teste)