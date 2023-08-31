from listaPilha import Pilha

pilha = Pilha()

pilha.push(12)
pilha.push(321)
pilha.push(32141)
pilha.push('ola')

print(pilha.itens)

if pilha.isEmpty():
    print("A pilha está vazia !")
else: print("A pilha tem elementos !")