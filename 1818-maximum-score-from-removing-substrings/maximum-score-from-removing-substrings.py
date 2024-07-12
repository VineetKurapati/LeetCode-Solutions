class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(s, pattern, score):
            stack = []
            count = 0
            for c in s:
                if c == pattern[1] and len(stack) > 0 and stack[-1] == pattern[0]:
                    stack.pop()
                    count += score
                else:
                    stack.append(c)
            return "".join(stack) , count
        if x > y:
            s, x_count = helper(s, "ab", x)
            s, y_count = helper(s, "ba", y)
        else:
            s, y_count = helper(s, "ba", y)
            s, x_count = helper(s, "ab", x)
        return x_count + y_count