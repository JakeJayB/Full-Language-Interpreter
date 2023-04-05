""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 3.1 - Parser for Expressions
    04/04/23
"""

import Parser

"""
def preOrder(tree):
    if tree == None:
        return
    # push data of node into stack
    preOrder(tree.left)
    preOrder(tree.middle)
    preOrder(tree.right)
"""

def evaluate(node):
    """Evaluate the operands of a single node"""
    if node is None:
        return None
    elif node.left is None and node.right is None:
        # leaf node
        return node.value
    else:
        # operator node
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val
        else:
            raiseError("Invalid operator")

def raiseError(e):
    print(f"SyntaxError :: {e}")
