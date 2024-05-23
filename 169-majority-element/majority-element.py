class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        res_ele = 0
        res_val = 0
        for num in d:
            if res_val < d[num]:
                res_ele = num
                res_val = d[num]
        return res_ele
        
        