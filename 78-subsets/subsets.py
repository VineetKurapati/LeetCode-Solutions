class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, temp):
            if i >= n:
                res.append(temp.copy())
                return
            temp.append(nums[i])
            backtrack(i+1, temp)
            temp.pop()
            backtrack(i+1 , temp)
        backtrack(0, [])
        return res