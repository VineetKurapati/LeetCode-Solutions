class Solution:
    def isHappy(self, n: int) -> bool:
        t = n
        s = set()
        while n!=1 and n not in s:
            sum_squares = 0
            s.add(n)
            while n>0:
                x = n % 10
                sum_squares += x*x
                n //= 10
            n = sum_squares
        return n == 1
        