class Pilha:
	def __init__(self) -> None:
		self.itens = []

	def __repr__(self) -> str:
		pointer = self.itens
		stringParaRetornar = str()
		for indice, elemento in enumerate(pointer):
			if indice == 0:
				stringParaRetornar += f"[{elemento}, "
			elif indice > 0:
				try:
					valor = pointer[indice + 1]
					stringParaRetornar += f"{elemento}, "
				except IndexError:
					stringParaRetornar += f"{elemento}]"
					break
		return stringParaRetornar

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