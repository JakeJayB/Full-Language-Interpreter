""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 3.1 - Parser for Expressions
    04/04/23
"""
from Scanner import TokenType
from Parser import Node

class EvaluatorStack:
    def __init__(self) -> None:
        EvaluatorStack.stack = []
        
        
def checkStack():
    if len(EvaluatorStack.stack) < 3: return
    tempArr = EvaluatorStack.stack[-3:]
    
    if tempArr[0].type != TokenType.SYMBOL: return
    elif tempArr[1].type != TokenType.NUMBER or tempArr[2].type != TokenType.NUMBER: return
    
    if tempArr[0].value == '+':
       EvaluatorStack.stack[-3] = Node(tempArr[1].value + tempArr[2].value, TokenType.NUMBER)
    elif tempArr[0].value == '-':
        EvaluatorStack.stack[-3] = Node(max(tempArr[1].value - tempArr[2].value, 0), TokenType.NUMBER)
    elif tempArr[0].value == '*':
        EvaluatorStack.stack[-3] = Node(tempArr[1].value * tempArr[2].value, TokenType.NUMBER)
    elif tempArr[0].value == '/':
        if tempArr[2].value == 0: raiseError("ZeroDivisionError => division by zero")
        EvaluatorStack.stack[-3] = Node(tempArr[1].value // tempArr[2].value, TokenType.NUMBER)
    else:
        raiseError("Invalid operator")
    
    EvaluatorStack.stack = EvaluatorStack.stack[:-2]
    
    
def preorderTraverse(node):
    """Evaluate the operands of a single node"""
    if node is None:
        return
    else:
        # operator node
        EvaluatorStack.stack.append(node)
        preorderTraverse(node.left)
        preorderTraverse(node.right)
        if node.type == TokenType.SYMBOL: checkStack()
        return


def evaluate(node):
    EvaluatorStack()
    preorderTraverse(node)
    return EvaluatorStack.stack

def raiseError(e):
    print(f"SyntaxError :: {e}")
