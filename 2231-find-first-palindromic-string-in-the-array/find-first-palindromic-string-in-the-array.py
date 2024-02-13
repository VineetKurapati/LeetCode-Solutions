class Solution:
    def isPalindrome(self, s):
        st = s[::-1]
        return s == st
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if self.isPalindrome(s):
                return s
        return ""