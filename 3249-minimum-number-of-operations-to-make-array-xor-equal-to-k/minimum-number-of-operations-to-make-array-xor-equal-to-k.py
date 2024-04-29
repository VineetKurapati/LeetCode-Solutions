class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        count = 0
        while k or curr:
            if (curr%2) != (k%2):
                count += 1
            k//=2
            curr//=2
        return count