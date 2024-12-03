class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        m = len(s)
        j = 0 
        res = ""
        for i in range(n):
            end = spaces[i]
            print(end)
            while j < end:
               res += s[j]
               j+=1
            res += " "
        while j < m:
            res += s[j]
            j += 1
        return res  