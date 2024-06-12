class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def happy(n):
            if n in s:
                return False
            if n == 1:
                return True
            count = 0
            s.add(n)
            while n > 0:
                t = (n % 10) ** 2 
                count += t
                n = n // 10
            return happy(count)
        return happy(n)
