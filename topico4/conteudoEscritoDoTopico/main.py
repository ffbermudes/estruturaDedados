from listaSimplesmenteEncadeada import ListaSimplesmenteEncadeada

lista = ListaSimplesmenteEncadeada()

lista.newNodo(123)
lista.newNodo(564)
lista.newNodo(53264)
lista.newNodo(56434)
lista.newNodo(56446)
lista.newNodo(5654314)

lista.buscaNaLista(56446)
print(lista.tamanhoDaLista)
lista.removeLastNode()
print(lista.tamanhoDaLista)