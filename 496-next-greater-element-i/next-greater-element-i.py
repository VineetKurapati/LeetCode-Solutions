class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums2:
            d[num] = -1
        n = len(nums2)
        for i in range(n):
            for j in range(i+1, n):
                if nums2[j] > nums2[i]:
                    d[nums2[i]] = nums2[j]
                    break
        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]
        return nums1