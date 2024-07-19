from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        
        def evaluate(a, b, operator):
            if operator == "+":
                return a + b
            if operator == "-":
                return b - a
            if operator == "*":
                return a * b
            if operator == "/":
                return int(b / a)
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                curr = evaluate(a, b, t)
                stack.append(curr)
        
        return stack[0]
