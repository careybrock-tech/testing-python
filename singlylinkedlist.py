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
    
    def append(self, lastvalue):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(lastvalue)
    def delete(self, value):
        current = self
        while current is not None:
            # find the specific node to delete
            if current.value == value:
                current.next = current.next.next
                return
            current = current.next
    def find(self, value):
        current = self
        while current is not None:
            # find the specific node in list
            if current.value == value:
                return True
            current = current.next
        return False
    def prepend(self, firstvalue):
        # Create a new node with the given value
        current_new_node_head = Node(firstvalue)
        # Set the new node's next to the current head
        current_new_node_head.next = self
        # Return the new node as the new head of the linked list
        return current_new_node_head
    
    # Note learn insert method and prepend method
    def insert(self, anyvalue, position):
        # Create a new node with the given value
        new_node = Node(anyvalue)
        # If the position is 0, insert at the beginning
        if position == 0:
            # Set the new node's next to the current head
            new_node.next = self
            return new_node
        # Traverse the list to find the node at the specified position
        current = self
        # Move to the node just before the specified position
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        # Insert the new node at the specified position
        new_node.next = current.next
        current.next = new_node
        return self
    def reverse(self):
        # Initialize pointers for the previous, current, and next nodes
        prev = None
        current = self
        while current is not None:
            # Store the next node
            next_node = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move the pointers one step forward
            prev = current
            current = next_node
        # Return the new head of the reversed linked list
        return prev
    def cycle(self):
        slow = self
        fast = self
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def length(self):
        current = self
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def remove_duplicates(self):
        current = self
        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return self
node1 = Node(10)
node2 = Node(1)   
node3 = Node(30)

node1.next = node2
node2.next = node3
node1.traverse()

result = node1.findthelowestvalue()
print(f"The lowest value is: {result}")