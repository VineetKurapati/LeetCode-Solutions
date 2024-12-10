class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        temp = ""
        res = 0
        for i in range(n):
            if temp == "" or temp[len(temp) - 1] == s[i]:
                temp += s[i]
            else:
                temp = s[i]
            count = 0 
            for j in range(n - len(temp) +1 ):
                if s[j : j + len(temp)] == temp:
                    count += 1
            if count >= 3:
                res = max(res, len(temp))
        if res == 0:
            return -1
        return res
            
            