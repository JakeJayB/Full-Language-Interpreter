""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 1.1 - Scanner for Expressions
    02/10/23
"""

from enum import Enum
import argparse
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


def keywordIndentifier(token):
    #TODO: implementation of keyword Indentifier
    keyWords = {"if", "then", "else", "endif", "while", "do", "endwhile", "skip"}

    if token.value in keyWords:
        token.type = TokenType.KEYWORD

    return token

def getTokens(line):
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
            # print(f"{newToken.value} : {newToken.type}")
            res.append(newToken)
            continue
        elif(re.match(r"[a-zA-Z]", line[i]) != None): # Identifiers
            newToken.type = TokenType.INDENTIFIER
            newToken.value = ""
            
            while i < len(line) and re.match(r"[a-zA-Z0-9]", line[i]) != None:
                newToken.value += line[i]
                i += 1
            
            #TODO: send identifier to keywordIdentifier() to check for keyword
            newToken = keywordIndentifier(newToken)
            
            # print(f"{newToken.value} : {newToken.type}")
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

            # print(f"{newToken.value} : {newToken.type}")
            res.append(newToken)
            continue
        else: # Errors
            newToken.value = str(line[i])
            i += 1
            # print(f"{newToken.value} : {newToken.type}")
            res.append(newToken)
            continue
    return res
            

def main(input, output):
    tokens = list()

    for line in input:
        output.write("Line: " + line.strip('\n') + "\n")
        tokens = getTokens(line)
        for token in tokens:
            if token.type == TokenType.ERROR:
                output.write(f"ERROR READING '{token.value}'\n")
                continue
            output.write(f"{token.value} : {TokenType.toString(token.type)}\n")
        output.write("\n")
        
            
    input.close()
    output.close()
        

ArgParser()