class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        """
        Initializes a Node with the given data.

        Parameters:
            data: Any - The data to be stored in the node.
        """
        self.data = data
        self.next = None

"""
Still, this implementation is not very efficient, and there is a drawback with the append method. 
In this, we have to traverse the entire list to find the insertion point. This may not be a problem 
when there are just a few items in the list, but it will be very inefficient when the list is long, 
as it will have to traverse the whole list to add an item every time. Let us discuss a better implementation of the append method.
"""

"""
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = node
            self.size += 1
"""

"""
For this, the idea is that we not only have a reference to the first node in the list but also 
have one more variable in the node that references the last node of the list. That way, we can quickly
append a new node at the end of the list. The worst-case running time of the append operation
can be reduced from O(n) to O(1) using this method. We must ensure that the previous last node
points to the new node that is to be appended to the list
"""
class SinglyLinkedList:
    """
    Initializes an empty singly linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_at_end(self, data):
        """
        Appends a new node with the given data at the end of the linked list.

        Parameters:
            data: Any - The data to be stored in the new node.
        """
        node = Node(data)
        
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.size += 1

    def append_at_beginning(self, data):
        """
        Appends a new node with the given data at the beginning of the linked list.

        Parameters:
            data: Any - The data to be stored in the new node.
        """
        node = Node(data)
        
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
            
        self.size += 1

    def insert_at_position(self, data, position):
        """
        Inserts a new node with the given data at the specified position in the linked list.

        Parameters:
            data: Any - The data to be stored in the new node.
            position: int - The position at which the new node will be inserted.
        """
        if position < 0 or position >= self.size:
            print("Invalid position")
            return
        
        if position == 0:
            self.append_at_beginning(data)
            return
    
        node = Node(data)
        current = self.head
        prev = 0
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1

        prev.next = node
        node.next = current

        if position == self.size:
            self.tail = node

        self.size += 1        

    def access_by_index(self, index):
        """
        Accesses the data of the node at the specified index in the linked list.

        Parameters:
            index: int - The index of the node to be accessed.

        Returns:
            Any - The data stored in the node at the specified index.
        """
        if index < 0 or index >= self.size:
            return f"Index out of bounds: There are only {self.size} elements."
        
        current = self.head
        count = 0
        
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1

    def find_by_value(self, value):
        """
        Finds the first occurrence of a node with the specified value in the linked list.

        Parameters:
            value: Any - The value to search for.

        Returns:
            Node or str - The node containing the specified value, or a message indicating that the value was not found.
        """
        current = self.head
        
        while current:
            if current.data == value:
                return current
            current = current.next
        
        return "The value you are looking for is not found." 
    
    def display(self):
        """
        Displays the elements of the linked list.

        Prints each element of the linked list separated by "-->", 
        followed by "null" to indicate the end of the list.
        """
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end = "--> ")
            currentNode = currentNode.next
        print("null")
    


singly = SinglyLinkedList()

singly.append_at_end(3)
singly.append_at_end(31)
singly.append_at_end(13)
singly.append_at_beginning(131)
singly.insert_at_position(40,2)

singly.display()