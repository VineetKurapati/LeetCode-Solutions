class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 0 
        for c in s:
            if c in seen:
                count += 1
                seen = set()
            seen.add(c)
        if seen:
            count += 1
        return count