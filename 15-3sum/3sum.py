class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    while l < r and nums[l] == temp[1]:
                        l += 1
                    while l < r and nums[r] == temp[2]:
                        r-=1
        return res
           