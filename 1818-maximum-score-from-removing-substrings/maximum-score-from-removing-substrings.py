class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, pair: str, gain: int) -> (str, int):
            stack = []
            count = 0
            for c in s:
                if stack and stack[-1] == pair[0] and c == pair[1]:
                    stack.pop()
                    count += gain
                else:
                    stack.append(c)
            return ''.join(stack), count

        if x > y:
            s, count_x = remove_pairs(s, "ab", x)
            s, count_y = remove_pairs(s, "ba", y)
        else:
            s, count_y = remove_pairs(s, "ba", y)
            s, count_x = remove_pairs(s, "ab", x)

        return count_x + count_y