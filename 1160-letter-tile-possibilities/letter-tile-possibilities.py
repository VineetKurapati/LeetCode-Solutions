class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        d = Counter(tiles)
        def backtrack(temp):
            nonlocal res
            if temp:
                res += 1
            for t in d:
                if d[t] != 0:
                    d[t] -=1 
                    backtrack(temp + t)
                    d[t] += 1
        backtrack("")
        return res
       