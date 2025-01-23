class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        left = 1
        right = 1 
        for i in range(len(nums)):
            left_prod.append(left)
            right_prod.append(right)
            left *= nums[i]
            right *= nums[(len(nums) -1 - i)]
        res = []
        for i in range(len(nums)):
            res.append(left_prod[i] * right_prod[(len(nums) - i - 1)])
        return res