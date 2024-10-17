class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                if current.next is None:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next

    def display(self):
        if self.is_empty():
            print("Linked list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a new linked list
my_list = LinkedList()

# Add nodes
my_list.add_at_head(3)
my_list.add_at_head(2)
my_list.add_at_head(1)
my_list.add_at_tail(4)
my_list.add_at_tail(5)

# Display the linked list
my_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Delete a node
my_list.delete(3)

# Display the updated linked list
my_list.display()  # Output: 1 -> 2 -> 4 -> 5 -> None