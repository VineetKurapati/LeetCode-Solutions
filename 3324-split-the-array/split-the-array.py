class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        print(c)
        for n in c:
            if c[n] > 2:
                return False
        return True