class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        def isOdd(n):
            if n == 1:
                return True
            return n%2 != 0
        for i in range(n-3+1):
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True
        return False