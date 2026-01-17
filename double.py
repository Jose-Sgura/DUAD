class Node:
    data=str
    next="Node"
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinked:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def prepend(self, data):
        new_node=Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()
    
    def print_backward(self):
        current= self.tail
        while current is not None:
            print(current.data, end="")
            if current.prev:
                print(" -> ", end="")
            current = current.prev
        print()

dll = DoubleLinked()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()
dll.print_backward()

dll.prepend("X")

dll.print_forward()
dll.print_backward()

dll.delete("B")

dll.print_forward()
dll.print_backward()
