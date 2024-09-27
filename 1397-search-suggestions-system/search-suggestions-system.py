class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        startswith = defaultdict(list)
        for p in products:
            c = ""
            for i in p:
                c += i
                startswith[c].append(p)
        c = ""
        res = []
        for char in searchWord:
            c += char
            t = sorted(startswith[c])[:3]
            res.append(t)
        return res