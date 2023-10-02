# linked list Implementaion :

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if not self.head:
            self.head= new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")

# Creating a linked list and adding elements

my_linked_list = linkedlist()
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)

my_linked_list.display()
            
