class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = float("-inf")
        while i <= j:
            current = (j-i) * min(height[i], height[j])
            res = max(current, res)
            if height[i] < height[j]:
                i+=1
            elif height[i] > height[j]:
                j-=1
            elif height[i] == height[j]:
                i+=1
                j-=1
        return res