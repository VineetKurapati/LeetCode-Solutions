class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for i in c:
            if c[i] > floor(n/2):
                return i
        return -1
