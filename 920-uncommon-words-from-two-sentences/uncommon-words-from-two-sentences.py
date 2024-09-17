class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        s1_set = Counter(s1)
        s2_set = Counter(s2)
        res = []
        for s in s1_set:
            if s1_set[s] > 1:
                continue
            if s not in s2_set:
                res.append(s)
        for s in s2_set:
            if s2_set[s] > 1:
                continue
            if s not in s1_set:
                res.append(s)
        return res