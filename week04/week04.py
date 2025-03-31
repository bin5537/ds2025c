class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def __str__(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.link
        return "end"

a_list = LinkedList()
a_list.append(8)
a_list.append(4)
a_list.append(-7)
print(a_list)
