class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_energy = 0 
        for n in nums:
            if curr_energy < 0:
                return False 
            if n > curr_energy:
                curr_energy = n 
            curr_energy -=1
        return True
        