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
    
# Counter.val acts as our 'i' for accessing elements in token array
class Counter():
    def __init__(self) -> None:
        Counter.val = 0
        
        
def printTree(node, output, whitespace=''):
    '''preorder traverse of tree'''
    
    if node == None: return
    output.write(whitespace + str(node.value) + " : " + str(node.type) + '\n')
    printTree(node.left, output, whitespace+'\t')
    printTree(node.middle, output, whitespace+'\t')
    printTree(node.right, output, whitespace+'\t')


# when error occurs, raiseError() is called
def raiseError(token, output):
    '''when error occurs, raiseError() is called'''
    
    output.write(f"SyntaxError: Invalid Parsing '{token}'")
    quit(0)


# Counter.val acts as our 'i' for accessing elements in token array
def consumeToken():
    Counter.val += 1


def parseExpr(tokens, output):
    if tokens == None: return

    tree = parseTerm(tokens, output)
    while Counter.val < len(tokens) and tokens[Counter.val].value == '+':
        consumeToken() 
        tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseTerm(tokens, output))

    return tree


def parseTerm(tokens, output):
    tree = parseFactor(tokens, output)
    while Counter.val < len(tokens) and tokens[Counter.val].value == '-':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseFactor(tokens, output))

    return tree


def parseFactor(tokens, output):
    tree = parsePiece(tokens, output)
    while Counter.val < len(tokens) and tokens[Counter.val].value == '/':
        consumeToken()
        tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parsePiece(tokens, output))

    return tree


def parsePiece(tokens, output):
    tree = parseElement(tokens, output)
    while Counter.val < len(tokens) and tokens[Counter.val].value == '*': 
        consumeToken()
        tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseElement(tokens, output))

    return tree


def parseElement(tokens, output):
    if Counter.val < len(tokens) and tokens[Counter.val].value == '(':
        consumeToken()
        tree = parseExpr(tokens, output) 
        if Counter.val < len(tokens) and tokens[Counter.val].value == ')':
            consumeToken()
            return tree
        else:
            raiseError("MISSING )", output)

    elif Counter.val < len(tokens) and tokens[Counter.val].type == Scanner.TokenType.NUMBER:
        consumeToken()
        #if next token isn't a symbol, raiseError()
        if Counter.val < len(tokens) and tokens[Counter.val].type != Scanner.TokenType.SYMBOL: raiseError(tokens[Counter.val].value, output)
        
        return Tree.MakeSubTree(tokens[Counter.val-1], None, None, None)
    elif Counter.val < len(tokens) and tokens[Counter.val].type == Scanner.TokenType.INDENTIFIER:
        consumeToken()
        #if next token isn't a symbol, raiseError()
        if Counter.val < len(tokens) and tokens[Counter.val].type != Scanner.TokenType.SYMBOL: raiseError(tokens[Counter.val].value, output)
        
        return Tree.MakeSubTree(tokens[Counter.val-1], None, None, None)
    else:
        raiseError(tokens[Counter.val].value, output)

            
def getAST(line, output):
    '''
    For external and importing use
    '''
    tokens = Scanner.getTokens(line, output)
    if tokens == []: return []
    
    output.write("Line: " + line.strip('\n') + "\n\n")
    output.write("Tokens:\n")
    for token in tokens:
        output.write(f"{token.value} : {Scanner.TokenType.toString(token.type)}\n")
    output.write("\n")
    
    # initializes Counter's 'val' attribute to 0
    Counter()
    root = parseExpr(tokens, output)
    return root

    