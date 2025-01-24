class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1 
        l, r = 0, 1
        charSet = set()
        n = len(s)
        res = float("-inf")
        charSet.add(s[l])
        while r < n:
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            res = max(res, (r - l + 1))
            charSet.add(s[r])
            r += 1
        return res