class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        watch = ['+', '-', '*', '/']
        def eval(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num2 - num1
            elif operator == '*':
                return num1 * num2
            else:
                return num2 / num1
        for token in tokens:
            if token not in watch:
                st.append(token)
            else:
                num1 = int(st.pop())
                num2 = int(st.pop())
                res = eval(num1, num2, token)
                st.append(res)
        return int(st.pop())
                