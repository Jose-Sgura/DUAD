class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
            self.data = data
            self.next = None

class stack:
    def __init__(self):
        self.top=None

    def push(self, data):
        new_node=Node(data)
        new_node.next=self.top
        self.top= new_node

    def pop(self):
        if self.top is None:
            print("Stack empty")
            return None
    
        removed_value = self.top.data
        self.top = self.top.next
        return removed_value

    def print_stack(self):
        current=self.top
        print("Stack")
    
        while current is not None:
            print(current.data)
            current=current.next

Stack=stack()

Stack.push(10)
Stack.push(20)
Stack.push(30)

Stack.print_stack()

Stack.pop()
Stack.print_stack()


