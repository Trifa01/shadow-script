class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return str(self.value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", value)
class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)
    
if __name__ == '__main__':
    s = "5.4+3"
    Lexer(s).tokenize()
    token = Token("INT", 1)
    integer = Integer(1)
