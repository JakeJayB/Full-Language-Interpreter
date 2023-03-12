""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 2.1 - Parser for Expressions
    03/10/23
"""
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
        Counter.val = -1
        Counter.next_token = None
        
# class Counter():
#     def __init__(self) -> None:
#         Counter.val = 0
        
        
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


# # Counter.val acts as our 'i' for accessing elements in token array
# def consumeToken():
#     Counter.val += 1


# def parseExpr(tokens, output):
#     if tokens == None: return

#     tree = parseTerm(tokens, output)
#     while Counter.val < len(tokens) and tokens[Counter.val].value == '+':
#         consumeToken() 
#         tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseTerm(tokens, output))

#     return tree


# def parseTerm(tokens, output):
#     tree = parseFactor(tokens, output)
#     while Counter.val < len(tokens) and tokens[Counter.val].value == '-':
#         consumeToken()
#         tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseFactor(tokens, output))

#     return tree


# def parseFactor(tokens, output):
#     tree = parsePiece(tokens, output)
#     while Counter.val < len(tokens) and tokens[Counter.val].value == '/':
#         consumeToken()
#         tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parsePiece(tokens, output))

#     return tree


# def parsePiece(tokens, output):
#     tree = parseElement(tokens, output)
#     while Counter.val < len(tokens) and tokens[Counter.val].value == '*': 
#         consumeToken()
#         tree = Tree.MakeSubTree(tokens[Counter.val-1], tree, None, parseElement(tokens, output))

#     return tree


# def parseElement(tokens, output):
#     if Counter.val < len(tokens) and tokens[Counter.val].value == '(':
#         consumeToken()
#         tree = parseExpr(tokens, output) 
#         if Counter.val < len(tokens) and tokens[Counter.val].value == ')':
#             consumeToken()
#             if Counter.val < len(tokens) and (tokens[Counter.val].type != Scanner.TokenType.SYMBOL or tokens[Counter.val].value == ')'): raiseError(tokens[Counter.val].value, output) 

#             return tree
#         else:
#             raiseError("MISSING )", output)

#     elif Counter.val < len(tokens) and tokens[Counter.val].type == Scanner.TokenType.NUMBER:
#         consumeToken()
#         #if next token isn't a symbol, raiseError()
#         if Counter.val < len(tokens) and tokens[Counter.val].type != Scanner.TokenType.SYMBOL: raiseError(tokens[Counter.val].value, output)
        
#         return Tree.MakeSubTree(tokens[Counter.val-1], None, None, None)
#     elif Counter.val < len(tokens) and tokens[Counter.val].type == Scanner.TokenType.INDENTIFIER:
#         consumeToken()
#         #if next token isn't a symbol, raiseError()
#         if Counter.val < len(tokens) and tokens[Counter.val].type != Scanner.TokenType.SYMBOL: raiseError(tokens[Counter.val].value, output)
        
#         return Tree.MakeSubTree(tokens[Counter.val-1], None, None, None)
#     elif Counter.val >= len(tokens):
#         raiseError("MISSING NUM OR ID AT END",output)
#     else:
#         raiseError(tokens[Counter.val].value, output)
        
        
        
# Counter.val acts as our 'i' for accessing elements in token array
def consumeToken(tokens):
    Counter.val += 1
    if Counter.val+1 >= len(tokens): 
        Counter.next_token = None 
        return
    Counter.next_token = tokens[Counter.val+1]
    
def parseStatement(tokens, output):
    tree = parseBaseStatement(tokens, output)
    while Counter.next_token != None and Counter.next_token.value == ';':
        temp = Counter.next_token
        consumeToken(tokens)
        tree = Tree.MakeSubTree(temp, tree, None, parseBaseStatement(tokens, output))
    return tree
    
def parseBaseStatement(tokens, output):
    if Counter.next_token != None and Counter.next_token == "skip":
        temp = Counter.next_token
        consumeToken()
        return Tree.MakeSubTree(temp, None, None, None)
    elif Counter.next_token != None and Counter.next_token == "if":
        pass
        # consumeToken()
        #return parseIfStatement()
    elif Counter.next_token != None and Counter.next_token == "while":
        pass
        # consumeToken()
        #return parseWhileStatement()
    elif Counter.next_token != None and Counter.next_token.type == Scanner.TokenType.INDENTIFIER:
        pass
        #return parseAssignment()
    else:
        raiseError("")

# TODO: implement parseAssignment
def parseAssignment(tokens, output):
    """
    if Counter.next_token.type == Scanner.TokenType.IDENTIFIER:
        temp = Counter.next_token
        consumeToken()
        if Counter.next_token == ':='
            consumeToken()
            return Tree.MakeSubTree(':=', Tree.MakeSubeTree(temp, None, None, None), None, parseExpr(tokens, output))
    """

# TODO: implement parseIfStatement
def parseIfStatement(tokens, output):
    """
    if Counter.next_token.type == Scanner.TokenType.KEYWORD:
        consumeToken()
        tree_1 = parseExpr(tokens, output)

        if Counter.next_token == "then":
            consumeToken()
            tree_2 = parseStatement(tokens, output)

        elif Counter.next_token == "else":
            consumeToken()
            tree_3 = parseStatement(tokens, output)

            if Counter.next_token == "endif":
                consumeToken()
                return Tree.MakeSubTree(tokens[Counter.val-1], tree_1, tree_2, tree_3)
    else:
        raiseError("")
    """

# TODO: implement parseWhileStatement
def parseWhileStatement(tokens, output):
    """
    if Counter.next_token == "while":
        consumeToken()
        tree_1 = parseExpr(tokens, output)
        if Counter.next_token == "do":
            consumeToken()
            tree_2 = parseStatement(tokens, output)
            if Counter.next_token == "endwhile":
                consumeToken()
                return Tree.MakeSubTree(tokens[Counter.val-1], tree_1, None, tree_2)
    else:
        raiseError("")
    """

def parseExpr(tokens, output):
    tree = parseTerm(tokens, output)
    while Counter.next_token != None and Counter.next_token.value == '+':
        temp = Counter.next_token
        consumeToken(tokens)
        tree = Tree.MakeSubTree(temp, tree, None, parseTerm(tokens, output))
    return tree


def parseTerm(tokens, output):
    tree = parseFactor(tokens, output)
    while Counter.next_token != None and Counter.next_token.value == '-':
        temp = Counter.next_token
        consumeToken(tokens)
        tree = Tree.MakeSubTree(temp, tree, None, parseFactor(tokens, output))

    return tree


def parseFactor(tokens, output):
    tree = parsePiece(tokens, output)
    while Counter.next_token != None and Counter.next_token.value == '/':
        temp = Counter.next_token
        consumeToken(tokens)
        tree = Tree.MakeSubTree(temp, tree, None, parsePiece(tokens, output))

    return tree


def parsePiece(tokens, output):
    tree = parseElement(tokens, output)
    while Counter.next_token != None and Counter.next_token.value == '*': 
        temp = Counter.next_token
        consumeToken(tokens)
        tree = Tree.MakeSubTree(temp, tree, None, parseElement(tokens, output))

    return tree

def parseElement(tokens, output):
    if Counter.next_token != None and Counter.next_token.value == '(':
        consumeToken(tokens)
        tree = parseExpr(tokens, output) 
        if Counter.next_token != None and Counter.next_token.value == ')':
            consumeToken(tokens)

            return tree
        else:
            raiseError("MISSING )", output)

    elif Counter.next_token != None and Counter.next_token.type == Scanner.TokenType.NUMBER:
        temp = Counter.next_token
        consumeToken(tokens)
                
        return Tree.MakeSubTree(temp, None, None, None)
    elif Counter.next_token != None and Counter.next_token.type == Scanner.TokenType.INDENTIFIER:
        temp = Counter.next_token
        consumeToken(tokens)
        
        return Tree.MakeSubTree(temp, None, None, None)
    elif Counter.next_token == None:
        raiseError("MISSING NUM OR ID AT END",output)
    else:
        raiseError(Counter.next_token.value, output)


            
def getAST(input, output):
    '''
    For external and importing use
    '''
    tokens = []
    for line in input:
        temp = Scanner.getTokens(line,output)
        if temp == []: continue
        tokens = tokens + temp
    if tokens == []: return []
    
    output.write("Tokens:\n")
    for token in tokens:
        output.write(f"{token.value} : {Scanner.TokenType.toString(token.type)}\n")
    output.write("\n")
    
    # initializes Counter's 'val' attribute to 0
    Counter()
    Counter.next_token = tokens[0]
    root = parseExpr(tokens, output)
    return root

    