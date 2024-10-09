class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        count = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return len(stack) + count