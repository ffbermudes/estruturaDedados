# Compreendendo estrutura de dados: Lista encadeada.

### Estrutura da classe -> LinkedList:

```
lista = {

    head: None
    
    append(data) : Void

    length() : int

    to_list() : Array

    display() : Void

    reverse_linked_list() : Void

}
```


Esse método será melhor demonstrado depois `reverse_linked_list()`.

**[linkedList.py]**

[linkedList.py]:linkedList.py

### Estrutura da classe -> Node:

```
Node = {

    constructor(data)

    dado = data,
    next = None

}
```

Essa classe será utilizada em todos nós da lista encadeada.

**[classNo.py]**

[classNo.py]: classNo.py


### LinkedList -> reverse_linked_list() : Void

Essa função tem o objetivo de inverter a ordem da lista ou colocar de trás para frente. É um método de manipulação dos nós que serão inseridos. Segue o código abaixo:

```
def reverse_linked_list(self):

    previous_node = None
    current_node = self.head
    
    while current_node != None:
        next = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next
    self.head = previous_node
```

Entendendo looping do método acima:

A forma que eu irei utilizar para explicar bem o que irá ocorrer em cada volta do loop será escrevendo os objetos de forma abstrata.

### Lista encadeada com 3 elementos

```
lista = {
    head: {

        data: 10,
        next: {

            data: 35,
            next: {

                data: 90,
                next: None
            }
        }
    
    }
}
```
Para poder compreender o loop vamos utilizar essa lista encadeada.

1. Volta um
