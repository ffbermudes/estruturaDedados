from no import Nodo

class ListaEncadeada:
	def __init__(self):
		self.head = None
		self.tamanhoDaLista = 0

	def insere(self, novoDado): # lista.insere(300) lista.insere(55) lista.insere(33)
		novoNodo = Nodo(novoDado) # {dado, proximo}
		novoNodo.proximo = self.head
		self.head = novoNodo
		self.tamanhoDaLista += 1

	def delete(self):
		if self.head == None:
			print("A lista já está vazia")

		else:
			self.head = self.head.proximo
			self.tamanhoDaLista -= 1