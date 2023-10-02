class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def sorted_descending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if data > current.next.data:
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")

            current = current.next
        print("None")


input_values = [6, 3, 4, 2, 1]

my_linked_list = LinkedList()
sorted_descending_list = LinkedList()

# 6 3 4 2 1
for value in input_values:
    my_linked_list.insert(value)

# 6 4 3 2 1
for value in input_values:
    sorted_descending_list.sorted_descending(value)

print("unsorted")
my_linked_list.display()
print("-----------------------------")
print("sorted")
sorted_descending_list.display()
