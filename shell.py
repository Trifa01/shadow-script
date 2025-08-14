from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

while True: 
    text = input("shadow script: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree)
    result = interpreter.interpreter()

    print(result)

