class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1 
        n = len(gas)
        count = 0
        start_index = 0
        for i in range(n):
            g = gas[i]
            c = cost[i]
            count += g - c 
            if count < 0:
                count =0 
                start_index = i + 1
        return start_index