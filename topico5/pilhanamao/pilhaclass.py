class Node:
	def __init__(self, dado):
		self.dado = dado
		self.anterior = None

	def __repr__(self) -> str:
		return f"{self.dado} -> {self.anterior}"

class Pilha:
	def __init__(self):
		self.top = None
		self.__size = 0

	def push(self, item):
		node = Node(item)
		node.anterior = self.top
		self.top = node
		self.__size +=1

	def __repr__(self):
		return str(self.top)

pilha = Pilha()
pilha.push(231)
pilha.push(555)

print(pilha)