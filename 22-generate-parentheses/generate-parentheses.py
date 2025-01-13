class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openp, closep):
            if openp == closep == n:
                res.append("".join(stack))
                return 
            if openp < n:
                stack.append("(")
                backtrack(openp + 1, closep)
                stack.pop()
            if openp > closep:
                stack.append(")")
                backtrack(openp, closep + 1)
                stack.pop()
        backtrack(0, 0)
        return res