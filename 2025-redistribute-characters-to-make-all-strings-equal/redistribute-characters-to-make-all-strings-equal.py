class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for word in words:
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1
        n = len(words)
        for c in d:
            if (d[c] % n != 0):
                return False
        return True