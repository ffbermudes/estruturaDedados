from node import Node

class LinkedList:
	def __init__(self):
		self.head = None
		self._size = 0

	def append(self, elemento):
		if self.head: #Tem que ser true None é false
			
			pointer = self.head
			#O Head vai se torna igual. Não faz sentindo o uso desse pointer.

			#Enquanto houver conteúdo no pointer next pointer vai ser igual ao ultimo elemento capturado. O loop vai garantir que no pointer vai estar o ultimo elemento da lista. O valor padrão do next é 0. zero é igual a false. Na primeira execução sempre passa sem entrar no loop.
			while(pointer.next):
				pointer = pointer.next
			#Independente do resultado acima o objeto Node será criado e inserido no pointer no atributo next
			pointer.next = Node(elemento)
		else:
			self.head = Node(elemento)
		self._size += 1

	def __len__(self):
		"""Retorna o tamanho da lista"""
		return self._size

	def get(self, index):
		pass

	def set(self, index, elemento):
		pass

	# def __getitem__(self, index):
	# 	pointer = self.head
	# 	for i in range(index):
	# 		if pointer:
	# 			pointer = pointer.next
	# 		else:
	# 			raise IndexError("list index out of range")
	# 	if pointer:
	# 		return pointer.data
	# 	else:
	# 		raise IndexError("list index out of range")

	# def __setitem__(self, index, elemento):
	# 	pointer = self.head
	# 	for i in range(index):
	# 		if pointer:
	# 			pointer = pointer.next
	# 		else:
	# 			raise IndexError("list index out of range")
	# 	if pointer:
	# 		pointer.data = elemento
	# 	else:
	# 		raise IndexError("list index out of range")