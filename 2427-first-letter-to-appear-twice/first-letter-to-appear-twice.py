class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for i,c in enumerate(s):
            if c not in d:
                d[c] = []
            d[c].append(i)
        res_index = float("inf")
        for c in d:
            if len(d[c]) > 1:
                temp = d[c][1]
                res_index = min(temp, res_index)
        return s[res_index]