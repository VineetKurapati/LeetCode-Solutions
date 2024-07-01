class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        l_product = 1
        for i in nums:
            prefix.append(l_product)
            l_product *= i
        r_product = 1
        for i in range(len(nums) -1, -1, -1):
            suffix.append(r_product)
            r_product *= nums[i]
        suffix.reverse()
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res