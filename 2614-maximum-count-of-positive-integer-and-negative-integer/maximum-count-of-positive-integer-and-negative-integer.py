class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = sum([1 for n in nums if n < 0])
        positive = sum([1 for n in nums if n > 0])
        return max(positive, negative)