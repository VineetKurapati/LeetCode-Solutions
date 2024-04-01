class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        n = len(words)
        return len(words[n-1])