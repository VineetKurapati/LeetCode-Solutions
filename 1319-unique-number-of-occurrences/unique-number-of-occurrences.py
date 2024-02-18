class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        t = {}
        for key in d:
            temp = d[key]
            if temp in t:
                return False
            else:
                t[temp] = key
        return True
