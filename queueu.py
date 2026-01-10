class Node:
    data:str
    next="Node"
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None
    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:

            self.head = new_node
            self.tail = new_node
        else:
            
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if self.head is None:
            print("Queue empty")
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            
            self.tail = None

        return removed_data
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_list()

q.dequeue()      
q.print_list()