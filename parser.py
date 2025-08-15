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
        if self.token.type.startswith("VAR"):
            return self.token 
    
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
    
    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token
    
    def statement(self):
        if self.token.type == "DECL": 
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token 
                self.move()
                right_node = self.expression()
            return [left_node, operation, right_node]
            # var assignment
        elif self.token.type == "INT" or self.token.type == "FLOAT" or self.token.type == "OP": 
            # Arithmetic expression
            self.expression()

    def parse(self):
        return self.statement()