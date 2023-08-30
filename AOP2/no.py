class Nodo:
	def __init__(self, proximoNodo = None):
		self.proximo = proximoNodo

	def __repr__(self):
		return f"{self.dado} -> {self.proximo}"