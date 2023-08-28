from classNode import Node

class CircularList:
    def __init__(self, default = None) -> None:
        self.inicio = default
        self.length = 0

    def insereNoInicio(self, dado):
        novoNodo = Node(dado) #Node -> {dado, proximo}
        nodoTemporario = self.inicio
        novoNodo.proximo = self.inicio
        if self.inicio is not None:
            while(nodoTemporario.proximo != self.inicio):
                nodoTemporario = nodoTemporario.proximo
            nodoTemporario.proximo = novoNodo
        else:
            novoNodo.proximo = novoNodo
        self.inicio = novoNodo
        self.length += 1