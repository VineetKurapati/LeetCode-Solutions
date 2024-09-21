class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        v = []
        for i in range(1, n+1):
            v.append(str(i))
        v.sort()
        r = []
        for i in v:
            r.append(int(i))
        return r
        