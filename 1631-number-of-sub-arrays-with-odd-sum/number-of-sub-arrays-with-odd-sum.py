class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = 0
        prefix = 0 
        odd, even = 0,1
        for a in arr:
            prefix += a 
            if prefix % 2 == 0:
                count += odd 
                even +=1 
            else:
                count += even 
                odd +=1
        return count % (10 ** 9 +7)