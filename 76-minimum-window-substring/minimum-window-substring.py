class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        countT, countS = Counter(t), {}
        res, reslen = [-1, -1], float("inf")
        l = 0 
        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l : r+ 1] if reslen != float("inf") else ""