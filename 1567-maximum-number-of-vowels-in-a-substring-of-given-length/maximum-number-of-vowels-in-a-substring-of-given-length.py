class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        currSum = 0
        res = 0
        l= 0
        for i in range(n):
            if s[i] in vowels:
                currSum += 1
            if i-l+1>k:
                if s[l] in vowels:
                    currSum -=1
                l+=1
            res = max(res, currSum)
        return res
        
