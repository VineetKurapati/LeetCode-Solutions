class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        nums[:] = [i for i in nums if i != val]
        return len(nums)