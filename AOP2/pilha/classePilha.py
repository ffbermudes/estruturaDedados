class Node:
    def __init__(self, dado:int) -> None:
        self.dado = dado
        self.anterior = None

    def __repr__(self) -> str:
        return f"{self.dado} -> {self.anterior}"

class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def __repr__(self) -> str:
        return str(self.top)

    # Insere um elemento no inicio da lista
    def push(self, item:int):
        node = Node(item) # Cria um nó que vai ser inserido no topo da pilha
        node.anterior = self.top #Definindo todo encadeamento da pilha em baixo do novo nó.

        self.top = node #inserindo novo nó na pilha juntamente com todo encadeamento
        self.size += 1 #incrementando mais 1 no tamanho da pilha

    # Remove o elemento do topo da pilha e a atualiza o tamanho da mesma removendo 1. Seguindo padrão Lifo
    def pop(self)-> None:
        if self.size > 0: # Checando se a lista não está vazia
            node = self.top
            self.top = self.top.anterior
            self.size -= 1 # Subtraindo tamanho da lista em um (1)
        else: print('Lista vazia')
    # Método para minha comprenssão de como a pilha está. Aqui eu consegui perceber que os elementos que foram inseridos primeiro estão no topo da pilha.
    def percorreTodaPilha(self) -> None:
        pointer = self.top
        lenPilha = self.size

        for i in range(lenPilha):
            print(pointer.dado)
            pointer = pointer.anterior
        print("Loop Terminado !")

    # Aqui só iremos retornar algum valor se houver algo na pilha. Caso o valor de top seja None printo uma negativa a respeito.
    def peek(self) -> int:
        if self.size > 0: # validando se existe alguma coisa dentro da pilha
            return self.top.dado
        print("A pilha está vazia") # nagativa

    # Método para validação da abertura e fechamento dos parenteses.

    # 1 - Para começar só vai entrar na pilha se for parenteses abrindo.

    # 2 - Caso a string no loop seja parenteses fechando e a pilha esteja vazia retornarei false pois não podemos começar expressões matemáticas com parenteses fechando.

    # 3- Caso seja parenteses fechando e a string a pilha possua conteudo ele vai remover da pilha o ultimo aberto.

    # 4- retorna booleano com a informação que eu preciso se a lista está vazia, caso esteja, irei perguntar se o valor é None para retornar verdadeiro
    def balanceamentoDeParenteses(self, s:str) -> bool:
        for char in s: #Percorrendo toda a string
            if char == "(": #1
                self.push(char) # 1
            elif char == ')': #2
                if self.size == 0: #2
                    return False #2
                self.pop() #3
        return self.size == 0 # 4

pilha = Pilha() #Construída a pilha

# Testes realizados com sucesso
print(pilha.balanceamentoDeParenteses('(()()()())')) #True
print(pilha.balanceamentoDeParenteses('(((())))')) #True
print(pilha.balanceamentoDeParenteses('(()((())()))')) #True
print(pilha.balanceamentoDeParenteses('((((((())')) #False
print(pilha.balanceamentoDeParenteses('()))')) #False
print(pilha.balanceamentoDeParenteses('(()()(()')) #False

