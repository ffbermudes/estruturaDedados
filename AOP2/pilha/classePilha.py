class Pilha:
	def __init__(self) -> None:
		self.itens = []

	def push(self, item):
		self.itens.insert(0, item)

	def pop(self):
		return self.itens.pop(0)

	def isEmpty(self):
		return self.itens == []

	def peek(self):
		return self.itens[0]

	def size(self):
		return len(self.itens)

	def checkParenteses(self):
		pointer = self.itens
		abriu = 0
		fechou = 0
		balanceado = bool()
		for indice, elemento in enumerate(pointer):
			if elemento == "(":
				abriu += 1
			elif elemento == ")":
				fechou += 1

		resultado = abriu == fechou
		print(resultado)


pilha = Pilha()
pilha.push("(")
pilha.push("(")
pilha.push(")")
pilha.push(")")

pilha.checkParenteses()