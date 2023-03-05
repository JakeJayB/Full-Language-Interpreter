import argparse
import Scanner

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
        
# i is our global iterator for each token list
i = 0   

def printTree(node, whitespace):
    if node == None: return
    print(whitespace + str(node.value))
    printTree(node.left, whitespace+'\t')
    printTree(node.middle, whitespace+'\t')
    printTree(node.right, whitespace+'\t')

def raiseError():
    pass

def consumeToken(tokens):
    global i
    # i= i+1
    if i >= len(tokens): pass
    i+=1



# 3 * (5 + 2 / x - 1)

def parseExpr(tokens):
    if tokens == None: return

    tree = parseTerm(tokens)
    while tokens[i].value == '+':
        consumeToken() 
        tree = Tree.MakeSubTree('+', tree, None, parseTerm(tokens))

    return tree

def parseTerm(tokens):
    tree = parseFactor(tokens)
    while tokens[i].value == '-':
        consumeToken()
        tree = Tree.MakeSubTree('-', tree, None, parseFactor(tokens))

    return tree

# 3 * (5 + 2 / x - 1)

def parseFactor(tokens):
    tree = parsePiece(tokens)
    while tokens[i].value == '/':
        consumeToken()
        tree = Tree.MakeSubTree('-', tree, None, parsePiece(tokens))

    return tree

def parsePiece(tokens):
    tree = parseElement(tokens)
    while tokens[i].value == '*':   #[token1(type,value), token2, token3]
        consumeToken()
        tree = Tree.MakeSubTree('-', tree, None, parseElement(tokens))

    return tree

def parseElement(tokens):
    if tokens[i].value == '(':
        consumeToken()
        tree = parseExpr(tokens) 
        if tokens[i].value == ')':
            consumeToken()
            return tree
        else:
            raiseError()

    elif tokens[i].type == Scanner.TokenType.NUMBER:
        consumeToken()
        return Tree.MakeSubTree(tokens[i].value, None, None, None)
    elif tokens[i].type == Scanner.TokenType.INDENTIFIER:
        consumeToken()
        return Tree.MakeSubTree(tokens[i].value, None, None, None)
    else:
        print("ERROR")

# 3 * (5 + 2 / x - 1)

def main(input, output):
    tokens = list()

    for line in input:
        tokens = Scanner.getTokens(line)
        output.write("Line: " + line.strip('\n') + "\n")
        output.write("Tokens:\n")
        
        for token in tokens:
            output.write(f"{token.value} : {Scanner.TokenType.toString(token.type)}\n")
        output.write("\n")
        
        parseExpr(tokens)

            
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

    input = open(args.input, "r")
    output = open(args.output, "a")
    
    main(input, output)
    
def main(input, output):
    pass
        
ArgParser()