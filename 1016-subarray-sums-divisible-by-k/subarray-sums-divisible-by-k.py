from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        d = {0: 1}
        res = 0
        for num in nums:
            count += num
            t = count % k
            if t < 0:  
                t += k
            if t in d:
                res += d[t]
                d[t] += 1
            else:
                d[t] = 1
                
        return res
