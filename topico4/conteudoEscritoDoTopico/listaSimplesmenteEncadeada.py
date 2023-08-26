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

    def deleteInicio(self):
        if not self.inicio:
            print("A Lista está vazia")
            return
        
        self.inicio = self.inicio.proximo

    def removeFirstNode(self):
        if self.inicio == None:
            print("Não existem nós no momento.")
            return
        
        self.inicio = self.inicio.proximo
        self.tamanhoDaLista -= 1

    def removeLastNode(self):
        lastNodeRemove = self.inicio
        if lastNodeRemove == None:
            print("Não existem nós no momento.")
            return
        while lastNodeRemove.proximo.proximo != None:
            lastNodeRemove = lastNodeRemove.proximo
        lastNodeRemove.proximo = None
        self.tamanhoDaLista -= 1

    def limpaLista(self):
        while self.inicio != None:
            self.deleteInicio()

        self.tamanhoDaLista = 0

    def buscaNaLista(self, dadoBuscado):
        findNode = self.inicio
        if not findNode:
            print("Lista está vazia")
            return
        
        while findNode:
            print(findNode.dado)
            if findNode.dado == dadoBuscado:
                print(f"Dado buscado localizado: {dadoBuscado} -> True")
                return
            findNode = findNode.proximo