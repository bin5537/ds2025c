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

    def remove(self, target):
        current = self.head
        if current.data == target:
            self.head = self.head.link
            return
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
            previous, current = current, current.link

    def __str__(self):
        current = self.head
        out_texts = ""
        while current is not None:
            out_texts += f"{current.data} -> "
            current = current.link
        return out_texts + "end"

a_list = LinkedList()

for _ in range(5):
    a_list.append(random.randint(1, 10))

print("normal: ", a_list)
a_list.remove(10)
print("remove(10): ", a_list)
