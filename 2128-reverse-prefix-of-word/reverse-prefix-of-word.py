class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        min_idx = float("inf")
        n = len(word)
        for i in range(n-1, -1, -1):
            if word[i] == ch:
                min_idx = min(min_idx, i)
        if min_idx == float("inf"):
            return word
        res = word[:min_idx+1]
        res = res[::-1]
        res += word[min_idx+1:]
        return res