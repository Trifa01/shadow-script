from lexer import Lexer
while True: 
    text = input("shadow script: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)  