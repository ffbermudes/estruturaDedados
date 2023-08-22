from classNo import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        #pointer
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        
        # current_node receberá um novo nó na classe.
        current_node.next = new_node
        return
    
    def length(self):
        if self.head == None:
            return 0
        
        # ponteiro
        current_node = self.head
        total = 0

        while current_node:
            current_node = current_node.next
            total += 1
        return total

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    
    def display(self):
        contents = self.head

        if contents is None:
            print("List has no element")
        
        while contents:
            print(contents.data)
            contents = contents.next
        print("----------------------")

    def reverse_linked_list(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node

