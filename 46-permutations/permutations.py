class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        def dfs(temp):
            if len(temp) == n:
                res.add(tuple(temp))
                return 
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs(temp)
                    temp.pop()
        dfs([])
        return [i for i in res]