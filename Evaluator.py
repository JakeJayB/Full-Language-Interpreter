""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 3.2 - Evaluator for Full Language
    04/30/23
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
        val = getIndentifier(node, output)
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
    if target.type == TokenType.NUMBER: return target.value
    
    id = target.value
    if id not in Evaluator.memory: raiseError(f"NameError => name '{id}' is not defined", output)   
    return Evaluator.memory[id]     


def checkStack(output):
    if len(Evaluator.stack) < 3: return
    
    # in the form: [SYMBOL, ID, ID]
    tempArr = Evaluator.stack[-3:]
    
    # if array is not in the form above
    if tempArr[0].type != TokenType.SYMBOL: 
        return
    elif ((tempArr[1].type != TokenType.NUMBER and tempArr[1].type != TokenType.INDENTIFIER) or
          (tempArr[2].type != TokenType.NUMBER and tempArr[2].type != TokenType.INDENTIFIER)): 
        return
    
    
    operand1, operand2 = getIndentifier(tempArr[1], output), getIndentifier(tempArr[2], output)
    operator = tempArr[0].value
    
    # compute the arithmetic operation depending on the operator
    if operator == '+':
       Evaluator.stack[-3] = Node(operand1 + operand2, TokenType.NUMBER)
    elif operator == '-':
        Evaluator.stack[-3] = Node(max(operand1 - operand2, 0), TokenType.NUMBER)
    elif operator == '*':
        Evaluator.stack[-3] = Node(operand1 * operand2, TokenType.NUMBER)
    elif operator == '/':
        if operand2 == 0: raiseError("ZeroDivisionError => division by zero", output)
        Evaluator.stack[-3] = Node(operand1 // operand2, TokenType.NUMBER)
    
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
        

# for Phase 3.2 - Evaluator for Full Language
def evaluateAST(node, output):
    if node == None:
        output.write(f"Output: {node}")
        return

    Evaluator()
    Evaluator.AST = node
    while Evaluator.AST != None:    
        Evaluator.AST = evaluateFullLanguage(Evaluator.AST, output)
    outputMemory(output)


# for Phase 3.1 - Evaluator for Expressions
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
