class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h = sorted(happiness)
        i = len(h) - 1
        count = 0
        t = 0
        temp_k = k
        while i>=0 and temp_k > 0:
            print(temp_k)
            temp = h[i] - t
            if temp < 0:
                temp = 0
            count += temp
            t+=1
            temp_k-=1
            i-=1
        return count