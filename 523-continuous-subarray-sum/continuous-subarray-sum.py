class Solution:
    def checkSubarraySum(self, nums, k):
        count = 0 
        prefix_dict = {0: -1}
        for i, num in enumerate(nums):
            count = (count + num) % k 
            if count in prefix_dict:
                if i - prefix_dict[count] > 1:
                    return True
            else:
                prefix_dict[count] = i
        return False