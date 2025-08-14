from lexer import Lexer
from parser import Parser
while True: 
    text = input("shadow script: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)
    parser = Parser(tokens)
    print(parser.parse())  