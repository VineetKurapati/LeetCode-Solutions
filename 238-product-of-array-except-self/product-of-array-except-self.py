class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        left = 1
        for i in range(len(nums)):
            left_prod.append(left)
            left *= nums[i]
        right = 1   
        for i in range(len(nums) - 1, -1, -1):
            right_prod.append(right)
            right*= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(left_prod[i] * right_prod[(len(nums) - i - 1)])
        return res