class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        count = 0 
        i = 0
        j = 0 
        n = len(s1)
        m = len(s2)
        while i < n and j < m :
            if s1[i] == s2[j] or (chr(((ord(s1[i]) - ord('a') + 1) % 26) + ord('a')) == s2[j]):
                count += 1
                i += 1
                j +=1 
            else:
                i += 1
        return count == m