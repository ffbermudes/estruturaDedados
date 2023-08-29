class Cliente():
	def __init__(self, nome, valorDaConta):
		self.nome = nome
		self.valorDaConta = valorDaConta

	def __repr__(self):
		return f"{self.nome} - {self.valorDaConta}"