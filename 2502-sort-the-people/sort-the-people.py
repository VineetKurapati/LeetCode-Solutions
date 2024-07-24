class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for n, h in zip(names, heights):
            l.append((n, h))
        l.sort(key = lambda x : x[1], reverse = True)
        print(l)
        res = []
        for n, h in l:
            res.append(n)
        return res
