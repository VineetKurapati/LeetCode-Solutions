class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        unique = 0
        for n in arr:
            if n not in d:
                d[n] = 1
                unique +=1 
            else:
                d[n]+=1
        d = dict(sorted(d.items(), key=lambda item: item[1]))
        t = 0
        for item in d:
            if d[item] <= k:
                k -= d[item]
                t += 1
        return unique - t