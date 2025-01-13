class Solution:
    def reverse(self, x: int) -> int:
        low_range = pow(-2, 31)
        high_range = pow(2, 31) - 1
        negative = False
        if x < 0:
            negative = True 
        x = abs(x)
        t = 0 
        while x > 0:
            temp = x % 10
            t = (t * 10) + temp 
            x = x//10
        if negative:
            t = t * -1 
        if t <= low_range or t>= high_range:
            return 0
        return t
