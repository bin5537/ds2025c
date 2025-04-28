class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end = "->")

def insert(root, value):
    newNode = TreeNode()
    newNode.data = value

    if root is None:
        return newNode

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = newNode
                break
            current = current.left
        else:
            if current.right is None:
                current.right = newNode
                break
            current = current.right
    return root

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 1, 7, 100, 20]
    root = None

    # 1번째 원소 부터 마지막 원소까지
    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)    # 3->9->8->15->10

    find_number = int(input())
    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다.")
            break
        elif find_number < current.data:
            print(f"{find_number}을(를) 못찾았습니다.")
            break
        else:
            if current.right is None:
                print(f"{find_number}을(를) 못찾았습니다.")
                break
            current = current.data
