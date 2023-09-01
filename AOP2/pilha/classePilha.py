class Pilha:
	def __init__(self) -> None:
		self.itens = []

	def push(self, item):
		self.itens.insert(0, item)

	def recebeStringCompleta(self, string:str):
		for char in string:
			self.push(char)
		resultado = self.checkParenteses()
		return resultado

	def pop(self):
		return self.itens.pop(0)

	def isEmpty(self):
		return self.itens == []

	def peek(self):
		return self.itens[0]

	def size(self):
		return len(self.itens)

	def limpaLista(self):
		while self.itens:
			self.pop()
	
	def checkParenteses(self) -> bool:
		pointer = self.itens
		#Para poder ter acesso as elementos que foram inseridos primeiro.
		pointer.reverse()
		abriu = 0
		fechou = 0
		balanceado = bool()
		for indice, elemento in enumerate(pointer):
			if elemento == ")" and indice == 0:
				return False
			elif elemento == "(":
				abriu += 1
			elif elemento == ")":
				fechou += 1

		balanceado = abriu == fechou
		return balanceado

# Construida pilha
pilha = Pilha()

#Primeira String
resultado1 = pilha.recebeStringCompleta('(()()()())')
print(resultado1)
pilha.limpaLista()

#Segunda String
resultado2 = pilha.recebeStringCompleta('(((())))')
pilha.limpaLista()
print(resultado2)

#Terceira String
resultado3 = pilha.recebeStringCompleta('(()((())()))')
pilha.limpaLista()
print(resultado3)

#Quarto String
resultado4 = pilha.recebeStringCompleta('((((((())')
pilha.limpaLista()
print(resultado4)

#Quinta String
resultado5 = pilha.recebeStringCompleta('()))')
pilha.limpaLista()
print(resultado5)

#Sexta String
resultado6 = pilha.recebeStringCompleta('(()()(()')
pilha.limpaLista()
print(resultado6)