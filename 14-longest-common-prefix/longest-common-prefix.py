class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return 0
        if n == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, n):
            j = 0 
            while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[:j]
            if prefix == "":
                return ""
        return prefix