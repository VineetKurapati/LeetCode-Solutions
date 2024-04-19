class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        t = []
        for i in range(n):
            if nums[i] == key:
                t.append(i)
        for i in range(n):
            for j in t:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        return res
