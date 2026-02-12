class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self,head):
        self.head=head
    
    def bubble_sort(self):
        if not self.head:
            return
        
        changes=True

        while changes:
            changes=False
            current=self.head
            while current.next:
                if current.data > current.next.data:

                    current.data, current.next.data = current.next.data, current.data
                    
                    changes=True
                current = current.next

    def print_structure(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

third_node=Node("I am the third one")
second_node=Node("I am the second one", third_node)
first_node=Node("I am the first one", second_node)

linked=LinkedList(first_node)

linked.print_structure()
print("---setting-up----")
linked.bubble_sort()
linked.print_structure()


    