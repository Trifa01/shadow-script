class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None 

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        

def preorder(node):
    if node is None:
        return None
    preorder(node.left)
    preorder(node.right)
    print(node.val)


tree = BinaryTree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
preorder(tree.root)


