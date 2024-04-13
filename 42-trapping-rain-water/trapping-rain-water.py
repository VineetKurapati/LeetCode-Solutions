class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_height_right = [0] * n
        max_height_left = [0] * n
        count = 0
        curr_max = 0
        for i in range(n):
            h = height[i]
            max_height_left[i] = curr_max
            curr_max = max(curr_max, h)
        curr_max = 0
        for i in range(n-1, -1, -1):
            h = height[i]
            max_height_right[i] = curr_max
            curr_max = max(curr_max, h)
        for i in range(n):
            l = max_height_left[i]
            r = max_height_right[i]
            h = height[i]
            temp = min(l,r) - h
            if temp > 0:
                count += temp
        return count