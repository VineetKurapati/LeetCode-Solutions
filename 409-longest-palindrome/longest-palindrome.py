class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_ = set()
        ans = 0
        
        for i in range(len(s)):
            # If Current Char is already in Set,, then Remove it,, And Do increment Ans.
            if s[i] in set_:
                set_.remove(s[i])
                ans += 2 # Adding 2,, 1 for Current Looking Char, & Other 1 for Removed Char
            
            else:
                set_.add(s[i])
        
        # If Set has Something means,, there are Some Chars which are Occuring Odd Number of times
        # From them, we can take Only One Char,, at Middle of the Palindrome String
        return ans + 1 if set_ else ans 