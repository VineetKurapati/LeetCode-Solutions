class Solution:
    def check(self, num):
        if num == 0:
            return False
        digits = []
        n = num 
        while n:
            a = n % 10
            if a == 0:
                return False
            digits.append(a)
            n = n//10
        for i in digits:
            if num % i != 0:
                return False
        return True
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        res = []
        for i in range(l, r+1):
            if self.check(i):
                res.append(i)
        return res