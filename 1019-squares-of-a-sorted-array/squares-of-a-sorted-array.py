class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            t = num * num
            res.append(t)
        res.sort()
        return res
        