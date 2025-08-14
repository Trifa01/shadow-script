from tokens import Integer, Float

class Interpreter:
    def __init__(self,tree):
        self.tree = tree
    
    def read_INT(self, value):
        return int(value)
    def read_FLOAT(self, value):
        return float(value)

    def compute_binary(self, left, right,op):
        left_type = left.type
        right_type = right.type
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)
        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right
        return Integer(output) if left_type == "INT" and right_type == "INT" else Float(output)

    def interpreter(self, tree=None): # tree=None to be able to passt left_node and right_node
        if tree is None:
            tree = self.tree
        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpreter(left_node)    
        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpreter(right_node)
        operator = tree[1]
        return self.compute_binary(left_node, right_node, operator)