# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    # print function
    def PrintTree(self):
        print(self.data)
# Creating a root node
root = Node(27)
root.PrintTree()
