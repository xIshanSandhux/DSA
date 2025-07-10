class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes
node1.next = node2
node2.next = node3

# node1 is the head of the list
current = node1  # Start from head
while current:
    print(current.data)
    current = current.next
