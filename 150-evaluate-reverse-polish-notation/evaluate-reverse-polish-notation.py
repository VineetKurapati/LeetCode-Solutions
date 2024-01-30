class Solution:
    def eval(self, a, b, token):
        if token == "+":
            return a + b
        elif token == "-":
            return b - a
        elif token == "/":
            return int(b / a)
        else:
            return b * a

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", '/']

        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                val = self.eval(a, b, token)
                stack.append(val)
            else:
                stack.append(int(token))

        return int(stack.pop())
