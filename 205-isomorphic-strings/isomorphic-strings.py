class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        m = {}
        m1 = {}
        for i in range(n):
            if s[i] not in m:
                m[s[i]] = t[i]
            if t[i] not in m1:
                m1[t[i]] = s[i]
            if s[i] in m and m[s[i]] != t[i]:
                return False
            if t[i] in m1 and m1[t[i]] != s[i]:
                return False
        return True
