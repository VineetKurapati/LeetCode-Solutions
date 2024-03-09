class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        res = float("inf")
        for num in nums1:
            if num in nums2:
                if num >= res:
                    break
                res = min(num, res)
        return res if  res != float("inf") else -1