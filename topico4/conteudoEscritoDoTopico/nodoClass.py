class Node:
    def __init__(self, dado, next = None):
        self.dado = dado
        self.proximo = next

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"
    
    def setProximo(self, proximoNodo):
        self.proximo = Node(proximoNodo)