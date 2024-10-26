import math
from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        max_val = max(deliciousness)
        max_power = 2 ** (math.ceil(math.log2(2 * max_val))) 
        count = 0
        hash_table = defaultdict(int) 

        for num in deliciousness:
            power = 1
            while power <= max_power:
                complement = power - num
                if complement in hash_table:
                    count += hash_table[complement]
                power *= 2  
            hash_table[num] += 1

        return count % MOD
