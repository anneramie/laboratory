class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return
        
        last = self.head
        while last.next:
            last=last.next

        last.next=new_node

    def print_recursion(self,node):
        if node is None:
            return
        print(node.data)
        self.print_recursion(node.next)
    def start_recursion_traversal(self):
        self.print_recursion(self.head)
list = LinkList()
list.insert(11)
list.insert(2)
list.insert(1)
list.insert(7)
list.insert(18)
list.insert(5)

print("LinkList")
list.start_recursion_traversal()
