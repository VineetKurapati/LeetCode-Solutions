class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            k = target - num
            if k in d:
                return [i, d[k]]
            else:
                d[num] = i
        return [-1, -1]