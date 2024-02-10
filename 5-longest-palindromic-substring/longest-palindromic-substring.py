class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def expand_around(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        max_len = s[0]
        for i in range(len(s) - 1):
            odd = expand_around(i, i)
            even  = expand_around(i, i+1)

            if(len(odd) > len(max_len)):
               max_len = odd
            if(len(even) > len(max_len)):
                max_len = even
        return max_len