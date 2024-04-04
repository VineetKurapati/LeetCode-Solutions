class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "":
            return 0
        res = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            if ch == ")":
                temp = len(stack)
                res = max(temp, res)
                stack.pop()
        return res