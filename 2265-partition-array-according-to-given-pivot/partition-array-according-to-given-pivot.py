class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        equal = []
        for n in nums:
            if n < pivot:
                left.append(n)
            if n == pivot:
                equal.append(n)
            if n > pivot:
                right.append(n)
        res = []
        for n in left:
            res.append(n)
        for n in equal:
            res.append(n)
        for n in right:
            res.append(n)
        return res