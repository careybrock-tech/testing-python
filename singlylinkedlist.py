class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def traverse(self):
        current = self
        while current is not None:
            print(current.value)
            current = current.next
            print("Traversal completed.")
    def findthelowestvalue(self):
        current = self
        lowest_value = current.value
        while current is not None:
            if current.value < lowest_value:
                lowest_value = current.value
            current = current.next
        return lowest_value 
    
    def findthehighestvalue(self):
        current = self
        highest_value = current.value
        while current is not None:
            if current.value > highest_value:
                highest_value = current.value
            current = current.next
        return highest_value
    
    def append(self, value):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def delete(self, value):
        current = self
        while current is not None:
            if current.value == value:
                current.next = current.next.next
                return
            current = current.next
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self
        return new_node
    
    
    
node1 = Node(10)
node2 = Node(1)   
node3 = Node(30)

node1.next = node2
node2.next = node3
node1.traverse()

result = node1.findthelowestvalue()
print(f"The lowest value is: {result}")