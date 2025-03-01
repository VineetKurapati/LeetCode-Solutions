class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                nums[i - 1] = nums[i - 1] * 2
                nums[i] = 0
        res = [] 
        count = 0 
        for i in nums:
            if i == 0:
                count += 1
            else:
                res.append(i)
        while count:
            res.append(0)
            count -=1 
        return res