class Pilha:
    def __init__(self) -> None:
        self.itens = []

    def push(self, item):
        self.itens.insert(0, item)

    def pop(self):
        if self.itens:
            return self.itens.pop(0)
        return None

    def isEmpty(self):
        return not self.itens

    def size(self):
        return len(self.itens)

    def recebeStringCompleta(self, string: str) -> bool:
        self.itens.clear()
        for char in string:
            if char == "(":
                self.push(char)
            elif char == ")":
                if self.isEmpty():
                    return False  # Existe um ')' sem par correspondente.
                self.pop()
        return self.isEmpty()  # Se a pilha estiver vazia, então está balanceada.

# Testando o código:
pilha = Pilha()

print(pilha.recebeStringCompleta("(()()()())"))
print(pilha.recebeStringCompleta("(((())))"))
print(pilha.recebeStringCompleta("(()((())()))"))
print(pilha.recebeStringCompleta("((((((())"))
print(pilha.recebeStringCompleta("()))"))
print(pilha.recebeStringCompleta("(()()(()"))