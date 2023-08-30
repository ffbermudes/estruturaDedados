from lista import ListaEncadeada

lista = ListaEncadeada()
lista.insere("Geraldo", 320.23)
lista.insere("Filipe", 200.21)
lista.insere("Joaquim", 50.32)
lista.insere("Maria", 200.32)
lista.insere("Rosalina", 300.42)

resultado = lista.mediaGastos()
print(resultado)