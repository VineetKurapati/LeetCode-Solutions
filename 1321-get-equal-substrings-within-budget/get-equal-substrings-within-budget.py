class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        max_len = 0
        curr_cost = 0
        start = 0
        for i in range(n):
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                # Write logic for checking the cost 
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, (i-start+1))
        return max_len