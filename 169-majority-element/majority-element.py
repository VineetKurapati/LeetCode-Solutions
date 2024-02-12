class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        n = len(nums)
        for key in dict:
            value = dict[key]
            if value > n//2:
                return key
        return -1