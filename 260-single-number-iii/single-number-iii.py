from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers. The result is the XOR of the two unique numbers.
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in xor_all (i.e., find any differing bit between the two unique numbers)
        diff_bit = 1
        while (xor_all & diff_bit) == 0:
            diff_bit <<= 1
        
        # Step 3: Divide the numbers into two groups and find the unique number in each group
        num1 = 0
        num2 = 0
        for num in nums:
            if (num & diff_bit) == 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
