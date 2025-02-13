class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = {}
        for i in range(n):
            needed = target - nums[i]
            if needed in s:
                return [s[needed], i]
            s[nums[i]] =  i 
        return [-1, -1]