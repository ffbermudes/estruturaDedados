from no import Nodo
from cliente import Cliente

class ListaEncadeada:
	def __init__(self) -> None:
		self.head = None
		self.tamanhoDaLista = 0

	def insere(self, nome:str, gasto:float) -> None:
		# {nome, valorDaConta} - Cliente
		cliente = Cliente(nome, gasto) 
		no = Nodo(cliente)

		if self.head == None:
			self.head = no
			self.tamanhoDaLista += 1
			return

		current_node = self.head #Pointer
		while current_node.proximo != None:
			current_node = current_node.proximo
		current_node.proximo = no

		print("t")


	def delete(self) -> None:
		if self.head == None:
			print("A lista já está vazia")

		else:
			self.head = self.head.proximo
			self.tamanhoDaLista -= 1

	def mediaGastos(self) -> float:
		pass