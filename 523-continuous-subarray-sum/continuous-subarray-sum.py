class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = 0
        d = {0 : -1}
        res = 0
        for i, num in enumerate(nums):
            count = (count + num) % k
            if count in d :
                if (i - d[count]) > 1:
                    return True 
            else:
                d[count] = i
        return False