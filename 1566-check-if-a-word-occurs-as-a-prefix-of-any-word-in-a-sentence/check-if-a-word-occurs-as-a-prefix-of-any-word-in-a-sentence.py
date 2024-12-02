class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        d = {}
        n = len(sentence)
        sentence = sentence.split()
        for i in range(len(sentence)):
            r = ""
            for j in sentence[i]:
                r += j
                if r not in d:
                    d[r] = float("inf")
                d[r] = min(i + 1, d[r])
        if searchWord not in d:
            return -1
        return d[searchWord]