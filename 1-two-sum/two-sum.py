class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            curr_num = nums[i]
            for j in range(i+1, n):
                if curr_num + nums[j] == target:
                    return {i, j}
        return {-1, -1}