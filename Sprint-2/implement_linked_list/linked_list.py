class Node:
    """A private node structure that serves as the 'handle' for O(1) removal."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, item):
        """Adds an element to the start of the list. Returns the Node handle."""
        new_node = Node(item)
        
        if not self.head:
            # If the list is empty, both head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Insert at the beginning
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
        return new_node

    def pop_tail(self):
        """Removes and returns the element value from the end of the list."""
        if not self.tail:
            return None  # Or raise IndexError depending on preference
            
        popped_node = self.tail
        value = popped_node.value
        
        if self.head == self.tail:
            # Only one element in the list
            self.head = None
            self.tail = None
        else:
            # Move tail back and sever the link
            self.tail = self.tail.previous
            self.tail.next = None
            
        # Clean up pointers of the removed node
        popped_node.previous = None
        return value

    def remove(self, node: Node):
        """Removes a specific node directly using its handle in O(1) time."""
        if not node:
            return

        # Case 1: Node is the head
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None  # List is now empty
                
        # Case 2: Node is the tail
        elif node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None  # List is now empty
                
        # Case 3: Node is in the middle
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        # Completely isolate the removed node
        node.next = None
        node.previous = None
