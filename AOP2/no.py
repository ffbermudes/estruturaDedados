from cliente import Cliente

class Nodo:
	def __init__(self, client: Cliente, proximoNodo = None):
		self.dado = client # {nome, valorDaConta}
		self.proximo = proximoNodo

	def __repr__(self):
		return f"{self.dado} -> {self.proximo}"