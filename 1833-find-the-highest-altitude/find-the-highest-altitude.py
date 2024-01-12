class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        arr = []
        arr.append(0)
        temp = 0
        for i in range(n):
            temp+= gain[i]
            arr.append(temp)
        return max(arr)