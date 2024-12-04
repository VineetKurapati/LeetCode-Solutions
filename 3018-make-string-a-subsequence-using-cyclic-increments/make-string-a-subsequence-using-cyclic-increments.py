class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        count = 0 
        i = 0
        j = 0 
        n = len(s1)
        m = len(s2)
        while i < n and j < m :
            if s1[i] == s2[j] or (chr(((ord(s1[i]) - ord('a') + 1) % 26) + ord('a')) == s2[j]):
                if s1[i] == s2[j]:
                    print(f"{s1[i]} == {s2[j]}")
                if (chr(((ord(s1[i]) - ord('a') + 1) % 26) + ord('a')) == s2[j]):
                    print(f"{chr(((ord(s1[i]) - ord('a') + 1) % 26) + ord('a'))} == {s2[j]}")
                count += 1
                i += 1
                j +=1 
            else:
                print(f"{s1[i]} != {s2[j]} so incrementing i")
                i += 1
        print(count, m)
        return count == m