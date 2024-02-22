class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # This uses a concept called in degree 
        if n == 1:
            return 1
        d = {}
        d1 = {}
        for a in trust:
            ai = a[0]
            bi = a[1]
            if bi not in d:
                d[bi] = [ai]
            else:
                d[bi].append(ai)
            if ai not in d1:
                d1[ai] = [bi]
            else:
                d1[ai].append(bi)
        for person in d:
            if len(d[person]) == n-1 and person not in d1:
                return person
        return -1