class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(temp):
            nonlocal res 
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrack(temp)
                    temp.pop()
        res = []
        backtrack([])
        return res