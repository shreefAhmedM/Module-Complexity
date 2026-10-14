class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, item):
        new_node = Node(item)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
        return new_node

    def pop_tail(self):
        if not self.tail:
            return None 
            
        popped_node = self.tail
        value = popped_node.value
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            
        popped_node.previous = None
        return value

    def remove(self, node: Node):
        if not node:
            return

        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None 
                
        elif node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None 
                
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = None
        node.previous = None