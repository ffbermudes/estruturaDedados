from nodoClass import Node

class ListaSimplesmenteEncadeada:

    def __init__(self, nodo = None) -> None:
        self.inicio = nodo
        self.tamanhoDaLista = 0

    def escreveConteudo(self) -> str:
        mostrarNodos = ''
        nodoAtual = self.inicio
        while nodoAtual:
            mostrarNodos += f'{nodoAtual} --> '
            nodoAtual = nodoAtual.proximo
        return mostrarNodos 