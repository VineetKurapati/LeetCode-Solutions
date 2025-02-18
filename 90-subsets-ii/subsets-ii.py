class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        n = len(nums)
        nums.sort()
        def dfs(temp, i):
            if i >= n:
                s.add(tuple(temp.copy()))
                return
            temp.append(nums[i])
            dfs(temp, i + 1)
            temp.pop()
            dfs(temp, i + 1)
        dfs([], 0)
        return [i for i in s]