class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        r = [] 
        while i < n and j < m:
            if nums1[i] <=nums2[j]:
                r.append(nums1[i])
                i+=1
            else:
                r.append(nums2[j])
                j+=1
        if j < m:
            while j<m:
                r.append(nums2[j])
                j+=1
        if i < n:
            while i < n:
                r.append(nums1[i])
                i+=1
        if len(r) % 2 == 0:
            mid = r[len(r)//2]
            print(mid)
            mid1 = r[(len(r)//2 ) - 1]
            print(mid1)
            return (mid + mid1)/2
        return r[len(r)//2]