class Node:
    def __init__(self, dado:int) -> None:
        self.dado = dado
        self.anterior = None

    def __repr__(self) -> str:
        return f"{self.dado} -> {self.anterior}"
    
class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.__size = 0

    def __repr__(self) -> str:
        return str(self.top)
    
    def push(self, item:int):
        node = Node(item)
        node.anterior = self.top
        self.top = node
        self.__size += 1

    def percorreTodaPilha(self) -> None:
        pointer = self.top
        lenPilha = self.__size

        for i in range(lenPilha):
            print(pointer.dado)
            pointer = pointer.anterior
        print("Loop Terminado !")

    def recebeStringCompleta(self, s:str) -> None:
        print(s)

pilha = Pilha()
pilha.push(123)
pilha.push(1234)
pilha.push(12345)
# pilha.percorreTodaPilha()
pilha.recebeStringCompleta("TESTESÂO")