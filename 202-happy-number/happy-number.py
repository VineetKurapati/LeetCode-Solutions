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
                t = n % 10 
                t = t ** 2
                count += t
                n = n // 10
            print(count)
            return happy(count)
        return happy(n)
