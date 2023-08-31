from AOP2.listaEncadeada.no import Nodo

class Cliente(Nodo):
	def __init__(self, nome:str, valorDaConta:float) -> None:
		super().__init__()
		self.nome = nome
		self.valorDaConta = valorDaConta

	def __repr__(self) -> str:
		return f"{self.nome} - {self.valorDaConta}"

	def setNextNodo(self, nome:str, valorDaConta:float):
		self.proximo = Cliente(nome, valorDaConta)