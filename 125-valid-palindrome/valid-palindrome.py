class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for c in s:
            if c.isdigit():
                r += c
            if c.isalpha():
                r += c.lower()
        r1 = ""
        for i in range(len(r)-1, -1, -1):
            r1 += r[i] 
        return r == r1
        