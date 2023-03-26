""" Jacob Bejarano,  Wesly Barayuga
    Project Phase 2.2 - Parser for Full Language
    03/25/23
"""

import argparse
import Parser

def main(input, output):
    root = Parser.getAST(input, output)
    output.write("AST:\n")
    Parser.printTree(root, output)
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

    # input = open("input_file.txt", "r")
    # output = open("out.txt", "a")
    
    main(input, output)
    
        
ArgParser()



# Parser.py Main (a little incomplete)
# def main(input, output):
#     '''
#     used when running file directly
#     '''
#     for line in input:
#         tokens = Scanner.getTokens(line, output)
#         if tokens == []: continue

#         # initializes Counter's 'val' attribute to 0
#         Counter()

        
        
#         root = parseExpr(tokens, output)
#         printTree(root, output)
#         output.write("\n\n")
        
#     input.close()
#     output.close()



# Scanner.py Main
# def main(input, output):
#     tokens = list()

#     for line in input:
#         output.write("Line: " + line.strip('\n') + "\n")
#         tokens = getTokens(line, output)
#         for token in tokens:
#             output.write(f"{token.value} : {TokenType.toString(token.type)}\n")
#         output.write("\n")

            
#     input.close()
#     output.close()
