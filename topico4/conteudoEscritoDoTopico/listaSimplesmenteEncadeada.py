from nodoClass import Node

class ListaSimplesmenteEncadeada:

    def __init__(self, nodo = None) -> None:
        self.inicio = nodo
        self.tamanhoDaLista = 0

    def newNodo(self, dadoNodo):
        
        if self.inicio == None:
            self.inicio = Node(dadoNodo)
            return
        
        actualNode = self.inicio
        while actualNode.proximo is not None:
            actualNode = actualNode.proximo
        actualNode.proximo = Node(dadoNodo)
        self.tamanhoDaLista +=1

    def escreveConteudo(self):
        print(self.inicio)
        return self.inicio
