from no import Nodo

class Cliente(Nodo):
	def __init__(self, nome:str, valorDaConta:float, proximo:Nodo = None) -> None:
		self.nome = nome
		self.valorDaConta = valorDaConta
		self.proximo = proximo

	def __repr__(self) -> str:
		return f"{self.nome} - {self.valorDaConta}"

	def setNextNodo(self, nome:str, valorDaConta:float):
		self.proximo = Cliente(nome, valorDaConta)