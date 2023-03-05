import argparse
import Scanner

class Node():
    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type
        self.left = None
        self.middle = None
        self.right = None       

class Tree():
    def __init__(self, root) -> None:
        self.root = root
    
    def MakeSubTree(root, left=None, middle=None, right=None):
        root = Node(root.value, root.type)
        root.left = left
        root.middle = middle
        root.right = right
        return root
        
# i is our global iterator for each token list
i = 0   

def printTree(node, whitespace=''):
    if node == None: return
    print(whitespace + str(node.value) + " : " + str(node.type))
    printTree(node.left, whitespace+'\t')
    printTree(node.middle, whitespace+'\t')
    printTree(node.right, whitespace+'\t')

def raiseError():
    print("ERROR")
    quit(0)

def consumeToken():
    global i
    i+=1

# 3 * 5 + 2 / x - 1

def parseExpr(tokens):
    if tokens == None: return

    tree = parseTerm(tokens)
    while i < len(tokens) and tokens[i].value == '+':
        consumeToken() 
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseTerm(tokens))

    return tree

def parseTerm(tokens):
    tree = parseFactor(tokens)
    while i < len(tokens) and tokens[i].value == '-':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseFactor(tokens))

    return tree

# 3 * (5 + 2 / x - 1)

def parseFactor(tokens):
    tree = parsePiece(tokens)
    while i < len(tokens) and tokens[i].value == '/':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parsePiece(tokens))

    return tree

def parsePiece(tokens):
    tree = parseElement(tokens)
    while i < len(tokens) and tokens[i].value == '*':   #[token1(type,value), token2, token3]
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseElement(tokens))

    return tree

def parseElement(tokens):
    if i < len(tokens) and tokens[i].value == '(':
        consumeToken()
        tree = parseExpr(tokens) 
        if i < len(tokens) and tokens[i].value == ')':
            consumeToken()
            return tree
        else:
            raiseError()

    elif i < len(tokens) and tokens[i].type == Scanner.TokenType.NUMBER:
        consumeToken()
        return Tree.MakeSubTree(tokens[i-1], None, None, None)
    elif i < len(tokens) and tokens[i].type == Scanner.TokenType.INDENTIFIER:
        consumeToken()
        return Tree.MakeSubTree(tokens[i-1], None, None, None)
    else:
        raiseError()

# 3 * (5 + 2 / x - 1)

def main(input, output):
    for line in input:
        tokens = Scanner.getTokens(line)
        # print(str(tokens))
        
        # output.write("Line: " + line.strip('\n') + "\n")
        # output.write("Tokens:\n")
        
        for token in tokens:
            output.write(f"{token.value} : {Scanner.TokenType.toString(token.type)}\n")
        output.write("\n")
        
        root = parseExpr(tokens)
        printTree(root)

            
    input.close()
    output.close()
    
def ArgParser():
    """
        Arugment Parser for the arguments passed from command line
        
        @return: None
    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="Input File")
    argParser.add_argument("-o", "--output", help="Output File")
    args = argParser.parse_args()

    # input = open(args.input, "r")
    # output = open(args.output, "a")

    input = open("input_file.txt", "r")
    output = open("out.txt", "a")
    
    main(input, output)
    
        
ArgParser()