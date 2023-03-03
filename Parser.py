class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.middle = None
        self.right = None       
    
class Tree():
    def __init__(self, root) -> None:
        self.root = root
    
    def MakeSubTree(self, root, left, middle, right):
        root = Node(root.value)
        root.left = left
        root.middle = middle
        root.right = right
        return root
        
        
def printTree(node, whitespace):
    if node == None: return
    print(node.value)
    printTree(node.left, whitespace+'\t')
    printTree(node.middle, whitespace+'\t')
    printTree(node.right, whitespace+'\t')
    
        
