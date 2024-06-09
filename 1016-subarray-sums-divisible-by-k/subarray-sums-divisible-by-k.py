class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        d = {0: 1}
        res = 0
        for num in nums:
            count += num
            t = (count % k)
            if t in d:
                res += d[t]
            if t in d:
                d[t] += 1
            elif t not in d:
                d[t] = 1
        print(d)
        return res