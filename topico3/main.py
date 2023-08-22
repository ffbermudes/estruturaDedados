from linkedList import LinkedList

lista = LinkedList()
lista.append(300)
lista.append(30)
lista.append(3)
lista.append(90878978)

primeiroNode = lista.head

# while(primeiroNode):
#     primeiroNode = primeiroNode.next
#     if primeiroNode:
#     	print(primeiroNode.data)

print(primeiroNode.data)
print(primeiroNode.next.data)
print(primeiroNode.next.next.data)
print(primeiroNode.next.next.next.data)
