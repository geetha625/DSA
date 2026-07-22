class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
print(node1.data)                                   # 10

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node1.next=node2
print(node1.next.data)    # 10 20

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
print(node1.next.next.data)         # 10 20 30

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
head=node1
current=head
while current:
    print(current.data)
    current=current.next
