""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 3.1 - Parser for Expressions
    04/04/23
"""
from Scanner import TokenType
from Parser import Node
import copy

class Evaluator:
    def __init__(self) -> None:
        Evaluator.stack = []
        Evaluator.memory = dict()
        Evaluator.AST = None
        
    def clearStack():
        Evaluator.stack.clear()

    def clearMemory():
        Evaluator.memory.clear()
        
    def clearAST():
        Evaluator.AST = None
        
    def clearAll():
        Evaluator.stack.clear()
        Evaluator.memory.clear()
        Evaluator.AST = None

    def getStackValue(output):
        if len(Evaluator.stack) != 1: return 0 
        node = Evaluator.stack[0]
        val = getIndentifier(node.value, output) if node.type == TokenType.INDENTIFIER else node.value
        Evaluator.clearStack()
        return val
        
        
# def evaluateFullLanguage(node, output):
#     if node == None: return None
    
#     if node.value == ';': 
#         node.left = evaluateFullLanguage(node.left, output)
        
#         if node.left == None: 
#             return node.right
#         else: return node
#     elif node.value == ":=":
#         evaluateExpression(node.right, output)
#         Evaluator.memory[node.left.value] = Evaluator.getStackValue()
#         return None
#     elif node.value == "while":
#         evaluateExpression(node.left, output)
#         if Evaluator.getStackValue() > 0: 
#             node = Node.MakeSubTree(Node(';',TokenType.SYMBOL), node.right, None, node)
#             return node
#         else: 
#             return None


def evaluateFullLanguage(node, output):
    if node == None: return None

    if node.value == ';':
        temp_node = copy.deepcopy(node)
        temp_node.left = evaluateFullLanguage(temp_node.left, output)

        if temp_node.left == None:
            return temp_node.right
        else:
            return temp_node
    elif node.value == ":=":
        evaluateExpression(node.right, output)
        Evaluator.memory[node.left.value] = Evaluator.getStackValue(output)
        return None
    elif node.value == "while":
        evaluateExpression(node.left, output)
        if Evaluator.getStackValue(output) > 0:
            temp_node = Node.MakeSubTree(Node(';', TokenType.SYMBOL), node.right, None, node)
            return temp_node
        else:
            return None
    elif node.value == "if":
        evaluateExpression(node.left, output)
        condition = Evaluator.getStackValue(output)
        if condition > 0: 
            return node.middle
        else:
            return node.right

    elif node.value == "skip":
        return None

    
def getIndentifier(target, output):
    if target not in Evaluator.memory: raiseError(f"NameError => name '{target}' is not defined", output)   
    return Evaluator.memory[target]     

def checkStack(output):
    if len(Evaluator.stack) < 3: return
    
    tempArr = Evaluator.stack[-3:]
    if tempArr[0].type != TokenType.SYMBOL: return
    elif ((tempArr[1].type != TokenType.NUMBER and tempArr[1].type != TokenType.INDENTIFIER) or
          (tempArr[2].type != TokenType.NUMBER and tempArr[2].type != TokenType.INDENTIFIER)): return
    
    val1, val2 = 0, 0
    match (tempArr[1].type, tempArr[2].type):
        case (TokenType.NUMBER, TokenType.NUMBER): val1, val2 = tempArr[1].value, tempArr[2].value
        case (TokenType.NUMBER, TokenType.INDENTIFIER): val1, val2 = tempArr[1].value, getIndentifier(tempArr[2].value, output)
        case (TokenType.INDENTIFIER, TokenType.NUMBER): val1, val2 = getIndentifier(tempArr[1].value, output), tempArr[2].value
        case (TokenType.INDENTIFIER, TokenType.INDENTIFIER): val1, val2 = getIndentifier(tempArr[1].value, output), getIndentifier(tempArr[2].value, output)

    
    
    if tempArr[0].value == '+':
       Evaluator.stack[-3] = Node(val1 + val2, TokenType.NUMBER)
    elif tempArr[0].value == '-':
        Evaluator.stack[-3] = Node(max(val1 - val2, 0), TokenType.NUMBER)
    elif tempArr[0].value == '*':
        Evaluator.stack[-3] = Node(val1 * val2, TokenType.NUMBER)
    elif tempArr[0].value == '/':
        if val2 == 0: raiseError("ZeroDivisionError => division by zero", output)
        Evaluator.stack[-3] = Node(val1 // val2, TokenType.NUMBER)
    
    Evaluator.stack.pop()
    Evaluator.stack.pop()
    
    
def evaluateExpression(node, output):
    """Evaluate the operands of a single node"""
    if node is None:
        return
    else:
        # operator node
        Evaluator.stack.append(node)
        evaluateExpression(node.left, output)
        evaluateExpression(node.right, output)
        if node.type == TokenType.SYMBOL: checkStack(output)


def outputMemory(output):
    output.write("\nOutput: ")
    for i in Evaluator.memory:
        output.write(f"\n{i} = {Evaluator.memory[i]}")
        

def evaluateAST(node, output):
    if node == None:
        output.write(f"Output: {node}")
        return

    Evaluator()
    Evaluator.AST = node
    while Evaluator.AST != None:    
        Evaluator.AST = evaluateFullLanguage(Evaluator.AST, output)
    outputMemory(output)
    # output.write(f"Output: {Evaluator.stack[0].value}")


# def evaluateAST(node, output):
#     if node == None:
#         output.write(f"Output: {node}")
#         return

#     EvaluatorStack()
#     evaluateExpression(node, output)
#     output.write(f"Output: {EvaluatorStack.stack[0].value}")
    
def raiseError(e, output):
    output.write(f"SemanticError :: {e}")
    quit(0)
