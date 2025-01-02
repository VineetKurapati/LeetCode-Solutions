class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = []
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                count += 1
            l.append(count)
        print(l)
        for s, e in queries:
            r = l[s-1] if s-1 >=0 else 0
            res.append(abs(l[e] - r))
        return res
