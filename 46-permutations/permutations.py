class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(temp):
            if len(temp) == n:
                res.append(temp.copy())
                return 
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs(temp)
                    temp.pop()
        dfs([])
        return res
            
