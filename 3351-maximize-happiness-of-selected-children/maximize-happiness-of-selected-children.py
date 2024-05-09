class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h = sorted(happiness)
        i = len(h) - 1
        count = 0
        t = 0
        while i>=0 and k > 0:
            temp = h[i] - t
            if temp < 0:
                temp = 0
            count += temp
            t+=1
            k-=1
            i-=1
        return count