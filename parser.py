class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]
    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
    
    # <factor> := ( <expr> )
    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLOAT":
            return self.token
        if self.token.value == "(":
            self.move()
            expression = self.expression()
            return expression 
    
    def term(self):
        left_node = self.factor()
        self.move()
        output = left_node
        if self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.move()
            right_node = self.factor()
            self.move()
            output = [left_node, operation, right_node]
        return output
    
    def expression(self):
        left_node = self.term()
        output = left_node
        if self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.move()
            right_node = self.term()
            output = [left_node, operation, right_node]
        return output
    

    def parse(self):
        return self.expression()