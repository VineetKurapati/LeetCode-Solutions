class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            count = 0 
            for q in quantities:
                count += ceil(q/x)
            return count <= n
        l, r = 1, max(quantities)
        res = 0 
        while l <= r:
            x = (l + r)//2
            if can_distribute(x):
                res  = x
                r = x - 1
            else:
                l = x + 1
        return res
