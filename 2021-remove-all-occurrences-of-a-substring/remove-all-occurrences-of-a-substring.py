class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= m:
                curr = "".join(stack[-m:])
                if curr == part:
                    for i in range(m):
                        stack.pop()
        return "".join(stack)