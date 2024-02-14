class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list_pos = []
        list_neg = []
        for num in nums:
            if num >=0:
                list_pos.append(num)
            else:
                list_neg.append(num)
        res = []
        n = len(list_pos)
        m = len(list_neg)
        i = 0
        j = 0
        positive = False
        while i<n or j<m:
            if positive and j < m:
                res.append(list_neg[j])
                j+=1
                positive = False
            if not positive and i < n:
                res.append(list_pos[i])
                i+=1
                positive = True
        return res