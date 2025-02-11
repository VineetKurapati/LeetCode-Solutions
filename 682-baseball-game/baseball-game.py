class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a + b)
            elif o == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(a * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)