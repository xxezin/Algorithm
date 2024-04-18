# 1. 노드 클래스 만들기 - linked list로 구현해보자
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 2. 이진 탐색 트리에 데이터 넣기
class NodeMgmt:
    def __init__(self,head):
        self.head = head
    
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None: # 있으면 더 깊이
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value) # 없으면 그 자리에
                    break
            
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 탐색하기
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right       
        return False

# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)
# BST.insert(3)
# BST.insert(0)
# BST.insert(4)
# BST.insert(8)

# print(BST.search(1))
# print(BST.search(7))

