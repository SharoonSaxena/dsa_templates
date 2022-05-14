"""
Contains the template classes for Singly link list implemetation in python
"""


class Node:
    """A simple node of a Single Linked List"""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    """Points to the head and tail of a Single Linked List"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def insert_node(self, data: any, location: int) -> None:
        """Inserts a node into single linked list based on location

        Args:
            data (any): Data stores in node
            location (int): non-negative integer
        """
        new_node = Node(data)
        if self.head is None:  # when List is empty
            self.head = new_node
            self.tail = new_node
        else:  # List is not empty
            if location == 0:  # At begining
                new_node.next = self.head
                self.head = new_node
            elif location == 1:  # At last
                self.tail.next = new_node
                self.tail = new_node
            else:  # Somewhere in between
                index = 0
                current_node = self.head
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                new_node.next = current_node.next
                current_node.next = new_node

    def traverse(self):
        """Traverses and prints the contents of linked list"""
        if self.head is None:
            print("Single Linked List is Empty!")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

    def find_data(self, data):
        """Finds a data value in the link list

        Args:
            data (any): data to be found

        Returns:
            any: data which has been found
        """
        if self.head is None:
            return "Singly Linked List is Empty!"
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node.data
            current_node = current_node.next
        return "Element not found in Singly Linked List"
    
    def delete_node(self, location):
        
        

    
linklist = SingleLinkedList()
linklist.insert_node(1, 1)
linklist.insert_node(2, 1)
linklist.insert_node(3, 1)
linklist.insert_node(4, 1)
linklist.insert_node(0, 0)
linklist.insert_node(100, 0)

# linklist.traverse()

print(linklist.find_data(33))
