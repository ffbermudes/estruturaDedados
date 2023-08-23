from linkedList import LinkedList

lista = LinkedList()
lista.append(3333)
lista.append(4444)
lista.append(5555)

print(f"Objeto Node 1º -> lista.head.data = {lista.head.data}")
print('-'*20)

'''
lista = {
    head: {
        data: 3333,
        next: None
    }
}
'''

print(f"Objeto Node 2º -> lista.head.next.data = {lista.head.next.data}")
print('-'*20)

'''
lista = {
    head: {
        data: 3333,
        next: {
            data: 4444,
            next: None
        }
    }
}
'''

print(f"Objeto Node 3º -> lista.head.next.next.data = {lista.head.next.next.data}")
print('-'*20)

'''
lista = {
    head: {
        data: 3333,
        next: {
            data: 4444,
            next: {
                data: 5555,
                next: None
            }
        }
    }
}
'''