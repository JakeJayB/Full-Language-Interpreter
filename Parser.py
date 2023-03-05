import argparse

class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.middle = None
        self.right = None       

class Tree():
    def __init__(self, root) -> None:
        self.root = root
    
    def MakeSubTree(self, root, left=None, middle=None, right=None):
        root = Node(root.value)
        root.left = left
        root.middle = middle
        root.right = right
        return root
        
def printTree(node, whitespace):
    if node == None: return
    print(whitespace + str(node.value))
    printTree(node.left, whitespace+'\t')
    printTree(node.middle, whitespace+'\t')
    printTree(node.right, whitespace+'\t')

def consumeToken():
    print("")
    #temp

def parseExpr(tokens):
    if tokens == None: return

    for i in tokens:
        tree = parseTerm(currToken, tokens)
        while tokens[i+1] == '+':
            consumeToken() #temp
            tree = Tree.MakeSubTree('+', tree, None ,parseTerm(i, tokens))

    return tree

def parseTerm(i, tokens):
    for i in tokens:
        tree = parseFactor(i, tokens)
        while tokens[i+1] == '-':
            consumeToken()
            tree = Tree.MakeSubTree('-', tree, None, parseFactor(i, tokens))

    return tree

def parseFactor(i, tokens):
    for i in tokens:
        tree = parsePiece(i, tokens)
        while tokens[i+1] == '/':
            consumeToken()
            tree = Tree.MakeSubTree('-', tree, None, parsePiece(i, tokens))

    return tree

def parsePiece(i, tokens):
    for i in tokens:
        tree = parseElement(i, tokens)
        while tokens[i+1] == '*':
            consumeToken()
            tree = Tree.MakeSubTree('-', tree, None, parseElement(i, tokens))

    return tree

def parseElement(i, tokens):
    if tokens[i+1] == '(':
        consumeToken()
        tree = parseExpr(tokens)
    else:
        return #leaf node value



    
def ArgParser():
    """
        Arugment Parser for the arguments passed from command line
        
        @return: None
    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="Input File")
    argParser.add_argument("-o", "--output", help="Output File")
    args = argParser.parse_args()

    input = open(args.input, "r")
    output = open(args.output, "a")
    
    main(input, output)
    
def main(input, output):
    pass
        
ArgParser()