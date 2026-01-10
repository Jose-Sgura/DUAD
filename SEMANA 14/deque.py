class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
        self.left=None
        self.right=None
    
    def push_left(self,data):
        new_node=Node(data)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next=self.left
            self.left.prev=new_node
            self.left=new_node
    def push_right(self, data):
        new_node = Node(data)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
    
    def pop_left(self):
        if self.left is None:
            print("Deque empty")
            return None
        removed_value = self.left.data
        
        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        return removed_value
    
    def pop_right(self):
        if self.right is None:
            print("Deque empty")
            return None
        removed_value = self.right.data

        if self.left == self.right:
            self.left = None
            self.right = None

        else:
            self.right = self.right.prev
            self.right.next = None
            
        return removed_value
    
    def print_deque(self):
        current = self.left
        print("Deque:")

        while current is not None:
            print(current.data)
            current = current.next

dq = Deque()

dq.push_left(10)
dq.push_right(20)
dq.push_left(5)
dq.push_right(30)

dq.print_deque()

dq.pop_left()
dq.pop_right()

dq.print_deque()

        