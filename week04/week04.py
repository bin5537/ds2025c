import  random

class Node:
    def __init__(self, data, link = None):
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

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}은(는) 링크드 리스트에 존재하지 않습니다!"


    def __str__(self):
        current = self.head
        out_texts = ""
        while current is not None:
            out_texts += f"{current.data} -> "
            current = current.link
        return out_texts + "end"

a_list = LinkedList()

for _ in range(10):
    a_list.append(random.randint(1, 30))
print(a_list)
print(a_list.search(10))
