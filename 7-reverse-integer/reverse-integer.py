class Solution:
    def reverse(self, x: int) -> int:
        
        flag = False 
        if x < 0:
            flag = True 
            x = abs(x)
        count = 0 
        while x:
            c = x % 10 
            count = (count * 10) + c
            x //= 10
        if flag:
            count *= -1
        if -2**31 > count or count > 2**31:
            return 0
        return count