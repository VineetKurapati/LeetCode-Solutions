class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()
        def backtrack(i, temp):
            if i > len(nums):
                return
            if i == len(nums):
                s.add(tuple(temp))
                return 
            temp.append(nums[i])
            backtrack(i + 1, temp)
            temp.pop()
            backtrack(i + 1, temp)
        backtrack(0, [])
        t = [i for i in s]
        t.sort()
        return t
             