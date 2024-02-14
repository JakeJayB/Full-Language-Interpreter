""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 1.2 - Scanner for Full Language
    02/26/23
"""

from enum import Enum
import re

class TokenType(Enum):
    NUMBER = 1
    SYMBOL = 2
    INDENTIFIER = 3
    KEYWORD = 4
    ERROR = 5
    
    def toString(type):
        match type:
            case TokenType.NUMBER:
                return "NUMBER"
            case TokenType.SYMBOL:
                return "SYMBOL"
            case TokenType.INDENTIFIER:
                return "INDENTIFIER"
            case TokenType.KEYWORD:
                return "KEYWORD"
            case TokenType.ERROR:
                return "ERROR"
        
    
class Token:
    def __init__(self, type, value) -> None:
       self.type = type
       self.value = value  
       

def  checkTokenValidity(tokens, line, output):
    for token in tokens:
        if token.type == TokenType.ERROR: 
            output.write(f"SyntaxError :: Invalid Token '{token.value}' in: {line}")
            quit(0)
            

def keywordIndentifier(token):
    keyWords = {"if", "then", "else", "endif", "while", "do", "endwhile", "skip"}

    if token.value in keyWords:
        token.type = TokenType.KEYWORD
    return token


# for external and importing use
def getTokens(line, output):
    if line.strip() == "":
        return []

    res = list()
    i = 0
    while i < len(line):
        #If current char is whitespace or newline 
        if line[i] == " " or line[i] == "\n":
            i += 1
            continue
        
        #intializing the token for now
        newToken = Token(TokenType.ERROR, None)
        
        if(re.match(r"[0-9]", line[i]) != None): # Numbers
            newToken.type = TokenType.NUMBER
            newToken.value = 0
            
            while i < len(line) and re.match(r"[0-9]", line[i]) != None:
                newToken.value = 10 * newToken.value + int(line[i]) 
                i += 1
            res.append(newToken)
            continue
        elif(re.match(r"[a-zA-Z]", line[i]) != None): # Identifiers
            newToken.type = TokenType.INDENTIFIER
            newToken.value = ""
            
            while i < len(line) and re.match(r"[a-zA-Z0-9]", line[i]) != None:
                newToken.value += line[i]
                i += 1
            
            newToken = keywordIndentifier(newToken)
            
            res.append(newToken)
            continue
        elif(re.match(r"[\+|\-|\*|/|\(|\)|;|:]", line[i]) != None): # Symbols
            newToken.type = TokenType.SYMBOL
            newToken.value = str(line[i])
            i += 1

            if (i < len(line) and line[i] == "=" and line[i-1] == ":"):
                newToken.value += str(line[i])
                i += 1
            elif (line[i-1] == ":"):
                newToken.type = TokenType.ERROR

            res.append(newToken)
            continue
        else: # Errors
            newToken.value = str(line[i])
            i += 1
            res.append(newToken)
            continue
    checkTokenValidity(res, line, output)
    return res

    
