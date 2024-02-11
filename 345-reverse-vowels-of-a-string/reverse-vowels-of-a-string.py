class Solution:
    def reverseVowels(self, s: str) -> str:
        c = list(s)
        n = len(c)
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = n-1
        while left < right:
            while left < n and c[left].lower() not in vowels:
                left +=1
            while right >= 0 and c[right].lower() not in vowels:
                right -= 1
            if left < right:
                c[left], c[right] = c[right], c[left]
                left+=1 
                right -=1
        return "".join(c)

