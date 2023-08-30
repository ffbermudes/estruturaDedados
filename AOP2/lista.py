from no import Nodo
from cliente import Cliente

class ListaEncadeada:
	def __init__(self) -> None:
		self.head = None
		self.tamanhoDaLista = 0

	def insere(self, nome:str, gasto:float) -> None:
		cliente = Cliente(nome, gasto)
		'''
		cliente = {
			nome: nome,
			valorDaConta: gasto
		}
		'''
		no = Nodo(cliente)
		'''
		no = {
			dado: {
				nome,
				valorDaConta
			},
			proximo: None
		}
		'''

		if self.head == None:
			self.head = no
			self.tamanhoDaLista += 1
			return

		current_node = self.head #Pointer
		while current_node.proximo != None:
			current_node = current_node.proximo
		current_node.proximo = no
		self.tamanhoDaLista += 1

	def delete(self) -> None:
		if self.head == None:
			print("A lista já está vazia")

		else:
			self.head = self.head.proximo
			self.tamanhoDaLista -= 1

	def mediaGastos(self) -> float:
		current_node = self.head
		totGastos = 0
		tamanhoLista = self.tamanhoDaLista
		while current_node.proximo != None:
			totGastos += current_node.dado.valorDaConta
			print(totGastos)
			print(current_node.dado)
			current_node = current_node.proximo
		totGastos += current_node.dado.valorDaConta
		media = totGastos/tamanhoLista
		return f"A media de gastos do cliente é: R$ {media:.2f}"