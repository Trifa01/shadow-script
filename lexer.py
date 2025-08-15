from tokens import Integer, Float, Operation, Declaration, Variable
class Lexer:
    digits = "0123456789"
    operations = "+/*-()="
    stopwords = " "
    letters = "abcdefghijklmnpqrstuvwxyz"
    declerations = ["make"]
    def __init__(self, text):
        self.text = text
        self.idx = 0 
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None
    
    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()
                
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)  
                self.move()  
            
            elif self.char in Lexer.stopwords:
                self.move()  
                continue # do not append to tokens for this iteration
            
            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declerations:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)

        return self.tokens
    
    def extract_word(self):
        word = ""
        while self.idx < len(self.text) and self.char in Lexer.letters:
            word += self.char
            self.move()
        return word 

    def extract_number(self):
        number = ""
        isFloat = False
        while self.idx < len(self.text) and (self.char in Lexer.digits) or (self.char == "."):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)
    
    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx] 