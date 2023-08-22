from node import Node

class Teste:
    def __init__(self):
        self.conteudo = [Node(980), Node(232)]

    def testePointer(self):
        pointer = self.conteudo
        for n in pointer:
            print(n.data)
            print(n.next)            

minhaclasseteste = Teste()
minhaclasseteste.testePointer()