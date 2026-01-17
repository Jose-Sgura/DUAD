class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    def print_tree(self):
        print("Binary Tree:")
        self._print_pre_order(self.root)
    
    def _print_pre_order(self, node):
        if node is not None:
            print(node.data)
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)
tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

tree.print_tree()