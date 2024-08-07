class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = []
        c = 0
        for i in nums:
            left_sum.append(c)
            c+=i
        c = 0
        for i in range(len(nums) -1 , -1, -1):
            right_sum.append(c)
            c+=nums[i]
        right_sum.reverse()
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
