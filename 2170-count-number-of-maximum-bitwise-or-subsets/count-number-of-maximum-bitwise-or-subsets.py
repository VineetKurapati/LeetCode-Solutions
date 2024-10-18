class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        def backtrack(i, n, curr):
            nonlocal res
            if i >= n:
                return
            temp = curr
            curr = curr | nums[i]
            res.append(curr)
            backtrack(i+1, n, curr)
            backtrack(i+1, n, temp)
        n = len(nums)
        backtrack(0, n, 0)
        m = max(res)
        count = 0
        for i in res:
            if i == m:
                count +=1
        return count
