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
        

def printTree(node, output, whitespace=''):
    if node == None: return
    output.write(whitespace + str(node.value) + " : " + str(node.type) + '\n')
    printTree(node.left, output, whitespace+'\t')
    printTree(node.middle, output, whitespace+'\t')
    printTree(node.right, output, whitespace+'\t')

def raiseError(token, output):
    output.write(f"SyntaxError: Invalid Parsing: {token}")
    quit(0)

# i is our global iterator for each token list
i = 0   
def consumeToken():
    global i
    i +=1

def parseExpr(tokens, output):
    if tokens == None: return

    tree = parseTerm(tokens, output)
    while i < len(tokens) and tokens[i].value == '+':
        consumeToken() 
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseTerm(tokens, output))

    return tree

def parseTerm(tokens, output):
    tree = parseFactor(tokens, output)
    while i < len(tokens) and tokens[i].value == '-':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseFactor(tokens, output))

    return tree

def parseFactor(tokens, output):
    tree = parsePiece(tokens, output)
    while i < len(tokens) and tokens[i].value == '/':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parsePiece(tokens, output))

    return tree

def parsePiece(tokens, output):
    tree = parseElement(tokens, output)
    while i < len(tokens) and tokens[i].value == '*': 
        consumeToken()
        tree = Tree.MakeSubTree(tokens[i-1], tree, None, parseElement(tokens, output))

    return tree

def parseElement(tokens, output):
    if i < len(tokens) and tokens[i].value == '(':
        consumeToken()
        tree = parseExpr(tokens, output) 
        if i < len(tokens) and tokens[i].value == ')':
            consumeToken()
            return tree
        else:
            raiseError("MISSING ')'", output)

    elif i < len(tokens) and tokens[i].type == Scanner.TokenType.NUMBER:
        consumeToken()
        #if next token isn't a symbol, raiseError()
        if i < len(tokens) and tokens[i].type != Scanner.TokenType.SYMBOL: raiseError(tokens[i].value, output)
        
        return Tree.MakeSubTree(tokens[i-1], None, None, None)
    elif i < len(tokens) and tokens[i].type == Scanner.TokenType.INDENTIFIER:
        consumeToken()
        #if next token isn't a symbol, raiseError()
        if i < len(tokens) and tokens[i].type != Scanner.TokenType.SYMBOL: raiseError(tokens[i].value, output)
        
        return Tree.MakeSubTree(tokens[i-1], None, None, None)
    else:
        raiseError(tokens[i].value, output)

            
#For external use
def getAST(line, output):
    tokens = Scanner.getTokens(line, output)
    if tokens == []: return []

    root = parseExpr(tokens, output)
    return root

def main(input, output):
    global i
    for line in input:
        
        tokens = Scanner.getTokens(line, output)
        if tokens == []: continue
        
        output.write("Line: " + line.strip('\n') + "\n\n")
        output.write("Tokens:\n")
        for token in tokens:
            output.write(f"{token.value} : {Scanner.TokenType.toString(token.type)}\n")
        output.write("\n")
        
        root = parseExpr(tokens, output)
        i = 0
        printTree(root, output)
        output.write("\n\n")
        
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